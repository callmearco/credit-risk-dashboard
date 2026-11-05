import os, glob, psycopg
from dotenv import load_dotenv

load_dotenv()
conn = psycopg.connect(
    host=os.getenv('PGHOST'), port=os.getenv('PGPORT'),
    dbname=os.getenv('PGDATABASE'), user=os.getenv('PGUSER'),
    password=os.getenv('PGPASSWORD'), autocommit=True)

for path in sorted(glob.glob('sql/migrations/*.sql')):
    with open(path, encoding='utf-8') as f:
        sql = f.read()
    print(f'applying {os.path.bassename(path)} ...', end=' ')
    conn.execute(sql)
    print('ok')
conn.close()
