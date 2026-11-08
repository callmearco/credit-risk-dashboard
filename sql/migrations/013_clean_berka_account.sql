DROP TABLE IF EXISTS clean.berka_account CASCADE;
CREATE TABLE clean.berka_account AS
SELECT account_id::int    AS account_id,
       district_id::int   AS district_id,
       "date"::date       AS opened_date,
       CASE frequency WHEN 'POPLATEK MESICNE'   THEN 'monthly'
                      WHEN 'POPLATEK TYDNE'     THEN 'weekly'
                      WHEN 'POPLATEK PO OBRATU' THEN 'per_transaction' END AS statement_frequency
FROM raw.berka_account;
ALTER TABLE clean.berka_account ADD PRIMARY KEY (account_id);