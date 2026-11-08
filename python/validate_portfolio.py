import os, pandas as pd, psycopg
from dotenv import load_dotenv
load_dotenv()
conn = psycopg.connect(host=os.getenv('PGHOST'), port=os.getenv('PGPORT'), dbname=os.getenv('PGDATABASE'),
                       user=os.getenv('PGUSER'), password=os.getenv('PGPASSWORD'))
Q = {
 'loans with >=1 missed payment, % (15-25)': """
    SELECT 100.0 * count(DISTINCT s.loan_id) FILTER (WHERE p.loan_id IS NULL) / count(DISTINCT s.loan_id)
    FROM clean.syn_schedule s LEFT JOIN clean.syn_payment p USING (loan_id, installment_no)
    WHERE s.due_date <= '2025-12-31'""",
 'bad vintage vs rest, ratio (1.5-2.2)': """
    WITH m AS (SELECT l.loan_id, l.vintage_month BETWEEN '2024-03' AND '2024-09' AS bad,
                      bool_or(p.loan_id IS NULL) AS missed
               FROM clean.syn_loan l JOIN clean.syn_schedule s USING (loan_id)
               LEFT JOIN clean.syn_payment p USING (loan_id, installment_no)
               WHERE s.due_date <= '2025-12-31' GROUP BY 1, 2)
    SELECT (avg(missed::int) FILTER (WHERE bad)) / (avg(missed::int) FILTER (WHERE NOT bad)) FROM m""",
 'top-20 borrowers share, % (15-20)': """
    WITH c AS (SELECT client_id, sum(original_amount) a FROM clean.syn_loan GROUP BY 1)
    SELECT 100.0 * (SELECT sum(a) FROM (SELECT a FROM c ORDER BY a DESC LIMIT 20) t) / sum(a) FROM c""",
 'schedule principal = original amount, violations (0)': """
    SELECT count(*) FROM (SELECT s.loan_id FROM clean.syn_schedule s JOIN clean.syn_loan l USING (loan_id)
                          GROUP BY s.loan_id, l.original_amount HAVING abs(sum(s.principal_due) - l.original_amount) > 1) x""",
}
for name, sql in Q.items():
    print(f'{name:<55} {pd.read_sql(sql, conn).iloc[0, 0]:>10.2f}')