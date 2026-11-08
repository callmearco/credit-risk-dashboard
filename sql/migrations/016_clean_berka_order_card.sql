DROP TABLE IF EXISTS clean.berka_order CASCADE;
CREATE TABLE clean.berka_order AS
SELECT order_id::int AS order_id, account_id::int AS account_id, bank_to, account_to,
       amount::numeric(14,2) AS amount,
       CASE NULLIF(trim(k_symbol), '') WHEN 'SIPO' THEN 'household' WHEN 'UVER' THEN 'loan_payment'
            WHEN 'POJISTNE' THEN 'insurance' WHEN 'LEASING' THEN 'leasing' ELSE NULL END AS purpose
FROM raw.berka_order;
ALTER TABLE clean.berka_order ADD PRIMARY KEY (order_id);

DROP TABLE IF EXISTS clean.berka_card;
CREATE TABLE clean.berka_card AS
SELECT card_id::int AS card_id, disp_id::int AS disp_id, type AS card_type, issued::date AS issued_date
FROM raw.berka_card;
ALTER TABLE clean.berka_card ADD PRIMARY KEY (card_id);