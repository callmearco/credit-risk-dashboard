import sys, os, io
import numpy as np, pandas as pd, yaml, psycopg
from dotenv import load_dotenv

# ---------- клиенты: демография из Home Credit, регионы из Berka ----------
def gen_clients(cfg, rng, hc, districts):
    n = cfg['n_clients']
    base = hc.dropna(subset=['score_ext_2', 'score_ext_3']).sample(n, replace=True, random_state=cfg['seed'])
    score = 0.5 * base.score_ext_2.values + 0.5 * base.score_ext_3.values + rng.normal(0, 0.05, n)
    ctype = rng.choice(['Retail', 'SME'], n, p=[0.85, 0.15])
    industries = ['trade', 'construction', 'agri', 'manufacturing', 'transport', 'services', 'it']
    return pd.DataFrame({
        'client_id': np.arange(1, n + 1),
        'client_type': ctype,
        'age_years': base.age_years.values,
        'gender': base.gender.values,
        'income_annual': (base.income_annual.values * 0.9).round(0),
        'employment_type': base.employment_type.values,
        'family_status': base.family_status.values,
        'children': base.children.values,
        'region_id': rng.choice(districts.district_id.values, n, p=districts.inhabitants / districts.inhabitants.sum()),
        'industry_code': np.where(ctype == 'SME', rng.choice(industries, n, p=[.30, .20, .15, .12, .10, .08, .05]), None),
        'internal_score': np.clip((score * 1000).round(), 300, 900).astype(int),
        'onboarded_date': pd.Timestamp('2022-01-01') + pd.to_timedelta(rng.integers(0, 730, n), 'D'),
    })

# ---------- кредиты ----------
def gen_loans(cfg, rng, clients):
    n = cfg['n_loans']; P = cfg['products']; names = list(P)
    product = rng.choice(names, n, p=[P[p]['share'] for p in names])
    sme = clients.loc[clients.client_type == 'SME', 'client_id'].values
    ret = clients.loc[clients.client_type == 'Retail', 'client_id'].values
    client_id = np.where(product == 'sme', rng.choice(sme, n), rng.choice(ret, n))
    amount = np.empty(n); term = np.empty(n, int); rate = np.empty(n)
    for p in names:
        m = product == p; lo, hi = P[p]['amount']
        amount[m] = rng.lognormal(np.log((lo * hi) ** 0.5), 0.6, m.sum()).clip(lo, hi)
        term[m] = rng.choice(range(P[p]['term'][0], P[p]['term'][1] + 1, 12), m.sum())
        rate[m] = rng.uniform(*P[p]['rate'], m.sum())
    top = rng.choice(np.where(product == 'sme')[0], 20, replace=False); amount[top] *= 100     # концентрация

    start, end = pd.Timestamp(cfg['period_start']), pd.Timestamp(cfg['period_end'])
    disb = start + pd.to_timedelta(rng.integers(0, (end - start).days, n), 'D')
    df = pd.DataFrame({
        'loan_id': np.arange(1, n + 1), 'client_id': client_id, 'product_code': product,
        'branch_id': clients.set_index('client_id').loc[client_id, 'region_id'].values,
        'channel_code': rng.choice(list(cfg['channels']), n, p=list(cfg['channels'].values())),
        'currency_code': rng.choice(['KGS', 'USD'], n, p=[1 - cfg['usd_share'], cfg['usd_share']]),
        'original_amount': amount.round(-3), 'term_months': term, 'interest_rate': rate.round(4),
        'disbursement_date': disb.normalize(),
    })
    df['maturity_date'] = df.disbursement_date + pd.to_timedelta(df.term_months * 30, 'D')
    df['vintage_month'] = df.disbursement_date.dt.strftime('%Y-%m')
    df['collateral_type'] = df.product_code.map({p: P[p]['collateral'] for p in names})
    df['collateral_value'] = np.where(df.collateral_type == 'none', 0, (df.original_amount * rng.uniform(1.1, 1.6, n)).round(-3))
    df['is_restructured'] = rng.random(n) < cfg['restructure_share']
    df['restructured_date'] = np.where(df.is_restructured, df.disbursement_date + pd.to_timedelta(rng.integers(180, 540, n), 'D'), pd.NaT)
    return df

# ---------- аннуитетный график ----------
def gen_schedule(loans):
    r = loans.interest_rate.values / 12; n = loans.term_months.values; P = loans.original_amount.values
    A = P * r * (1 + r) ** n / ((1 + r) ** n - 1)
    balance = P.copy(); rows = []
    for k in range(1, n.max() + 1):
        active = k <= n
        interest = balance * r
        principal = np.where(active, np.minimum(A - interest, balance), 0)
        due = (loans.disbursement_date + pd.DateOffset(months=k)).values
        rows.append(pd.DataFrame({'loan_id': loans.loan_id.values[active], 'installment_no': k,
                                  'due_date': due[active], 'principal_due': principal[active].round(2),
                                  'interest_due': interest[active].round(2)}))
        balance = balance - principal
    s = pd.concat(rows, ignore_index=True)
    s['total_due'] = s.principal_due + s.interest_due
    return s

# ---------- платежи: марковская цепь по месяцам ----------
def gen_payments(cfg, rng, loans, schedule, clients):
    R = cfg['roll']; bad = cfg['bad_vintage']; end = pd.Timestamp(cfg['period_end'])
    score = clients.set_index('client_id').internal_score
    sched = {k: g.sort_values('installment_no') for k, g in schedule.groupby('loan_id')}
    out = []
    for ln in loans.itertuples():
        risk = cfg['products'][ln.product_code]['base_pd'] / 0.05
        risk *= np.interp(score[ln.client_id], [300, 900], [2.0, 0.5])
        if bad['from'] <= ln.vintage_month <= bad['to']: risk *= bad['pd_multiplier']
        if ln.channel_code == 'online': risk *= cfg['online_pd_multiplier']
        p_miss = min(0.35, R['p_miss_base'] * risk)
        missed = 0
        for inst in sched[ln.loan_id].itertuples():
            if inst.due_date > end: break
            if missed == 0:
                if rng.random() < p_miss: missed = 1; continue
                paid = inst.total_due
            else:
                u = rng.random(); cure = R['cure_from_1'] if missed == 1 else R['cure_from_2plus']
                if u < cure:                         paid = inst.total_due * (missed + 1); missed = 0
                elif u < cure + R['pay_current_only']: paid = inst.total_due
                else:                                missed += 1; continue
            out.append((ln.loan_id, inst.installment_no, inst.due_date + pd.Timedelta(days=int(rng.integers(0, 6))), round(paid, 2)))
    return pd.DataFrame(out, columns=['loan_id', 'installment_no', 'paid_date', 'amount_paid'])

# ---------- запись ----------
def write(conn, df, table):
    conn.execute(f'TRUNCATE {table} CASCADE')
    buf = io.StringIO(); df.to_csv(buf, index=False, header=False, date_format='%Y-%m-%d'); buf.seek(0)
    with conn.cursor().copy(f"COPY {table} ({', '.join(df.columns)}) FROM STDIN WITH (FORMAT csv)") as cp:
        cp.write(buf.read())
    print(f'{table:<22} {len(df):>12,}')

def main():
    load_dotenv()
    cfg_path = sys.argv[sys.argv.index('--config') + 1] if '--config' in sys.argv else 'python/config.yaml'
    cfg = yaml.safe_load(open(cfg_path)); rng = np.random.default_rng(cfg['seed'])
    with psycopg.connect(host=os.getenv('PGHOST'), port=os.getenv('PGPORT'), dbname=os.getenv('PGDATABASE'),
                         user=os.getenv('PGUSER'), password=os.getenv('PGPASSWORD'), autocommit=True) as conn:
        hc = pd.read_sql('SELECT age_years, gender, income_annual, employment_type, family_status, children, score_ext_2, score_ext_3 FROM clean.hc_application', conn)
        districts = pd.read_sql('SELECT district_id, inhabitants FROM clean.berka_district', conn)
        clients = gen_clients(cfg, rng, hc, districts);           write(conn, clients, 'clean.syn_client')
        loans = gen_loans(cfg, rng, clients);                     write(conn, loans, 'clean.syn_loan')
        schedule = gen_schedule(loans);                           write(conn, schedule, 'clean.syn_schedule')
        payments = gen_payments(cfg, rng, loans, schedule, clients); write(conn, payments, 'clean.syn_payment')

if __name__ == '__main__':
    main()

