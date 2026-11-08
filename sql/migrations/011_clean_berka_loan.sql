DROP TABLE IF EXISTS clean.berka_loan CASCADE;
CREATE TABLE clean.berka_loan AS
SELECT loan_id::int               AS loan_id,
       account_id::int            AS account_id,
       "date"::date               AS loan_date,
       amount::numeric(14,2)      AS amount,
       duration::int              AS duration_months,
       payments::numeric(14,2)    AS monthly_payment,
       status                     AS status_code,
       CASE status WHEN 'A' THEN 'closed_ok'      WHEN 'B' THEN 'closed_default'
                   WHEN 'C' THEN 'active_ok'      WHEN 'D' THEN 'active_overdue' END AS status
FROM raw.berka_loan;
ALTER TABLE clean.berka_loan ADD PRIMARY KEY (loan_id);