import pandas as pd
B = 'data/raw/berka/'
acc  = pd.read_csv(B + 'account.csv')
loan = pd.read_csv(B + 'loan.csv')
disp = pd.read_csv(B + 'disp.csv')
cli  = pd.read_csv(B + 'client.csv')
tr   = pd.read_csv(B + 'trans.csv')

print('loan->account ok:', loan.account_id.isin(acc.account_id).all())        # True
print('one loan per account:', not loan.account_id.duplicated().any())        # True
print('max clients per account:', disp.groupby('account_id').client_id.nunique().max())  # 2
print(loan.status.value_counts())                                             # A 203, C 403, B 31, D 45
print(cli.gender.value_counts())                                              # F / M
print('loans:', pd.to_datetime(loan['date']).min().date(), '..', pd.to_datetime(loan['date']).max().date())
print('trans:', pd.to_datetime(tr['date']).min().date(), '..', pd.to_datetime(tr['date']).max().date())
print(tr.k_symbol.fillna('<NULL>').str.strip().replace('', '<EMPTY>').value_counts())

uver = tr[tr.k_symbol.str.strip() == 'UVER'].groupby('account_id').amount.median()
chk = loan.set_index('account_id').payments.to_frame().join(uver.rename('uver_median'))
print((chk.payments.round(0) == chk.uver_median.round(0)).mean())  # близко к 1.0