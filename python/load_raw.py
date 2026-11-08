import os, psycopg
from dotenv import load_dotenv
load_dotenv()

BERKA = ['account', 'client', 'disp', 'district', 'loan', 'order', 'trans', 'card']
HC = {'hc_application': 'application_train', 'hc_installments': 'installments_payments', 'hc_bureau': 'bureau'}

FILES = {f'raw.berka_{t}': f'/data/raw/berka/{t}.csv' for t in BERKA}
FILES.update({f'raw.{t}': f'/data/raw/hc/{f}.csv' for t, f in HC.items()})

with psycopg.connect(host=os.getenv('PGHOST'), port=os.getenv('PGPORT'), dbname=os.getenv('PGDATABASE'),
                     user=os.getenv('PGUSER'), password=os.getenv('PGPASSWORD'), autocommit=True) as conn:
    for table, path in FILES.items():
        conn.execute(f'TRUNCATE {table}')
        conn.execute(f"COPY {table} FROM '{path}' WITH (FORMAT csv, HEADER true)")
        n = conn.execute(f'SELECT count(*) FROM {table}').fetchone()[0]
        print(f'{table:<24} {n:>12,}')