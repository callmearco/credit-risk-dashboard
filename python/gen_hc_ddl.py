import pandas as pd
cols = pd.read_csv('data/raw/hc/application_train.csv', nrows=0).columns
lines = ['', 'DROP TABLE IF EXISTS raw.hc_application;', 'CREATE TABLE raw.hc_application (']
lines.append(',\n'.join(f'    "{c.lower()}" text' for c in cols))
lines.append(');')
with open('sql/migrations/002_raw_raw_tables.sql', 'a', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
print(f'append {len(cols)} columns')