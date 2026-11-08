import os, sys, glob, psycopg
from dotenv import load_dotenv

load_dotenv()
start = sys.argv[sys.argv.index('--from') + 1] if '--from' in sys.argv else '000'

conn = psycopg.connect(
    host=os.getenv('PGHOST'), port=os.getenv('PGPORT'),
    dbname=os.getenv('PGDATABASE'), user=os.getenv('PGUSER'),
    password=os.getenv('PGPASSWORD'), autocommit=True)

for path in sorted(glob.glob('sql/migrations/*.sql')):
    name = os.path.basename(path)
    if name[:3] < start:
        continue
    with open(path, encoding='utf-8') as f:
        sql = f.read()
    print(f'applying {name} ...', end=' ')
    conn.execute(sql)
    print('ok')
conn.close()