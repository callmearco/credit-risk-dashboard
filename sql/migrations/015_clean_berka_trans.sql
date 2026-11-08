DROP TABLE IF EXISTS clean.berka_trans CASCADE;
CREATE TABLE clean.berka_trans AS
SELECT trans_id::bigint                AS trans_id,
       account_id::int                 AS account_id,
       "date"::date                    AS trans_date,
       CASE type WHEN 'PRIJEM' THEN 'credit' ELSE 'debit' END   AS direction,   -- VYDAJ и VYBER — расход
       CASE NULLIF(trim(operation), '')
            WHEN 'VKLAD'          THEN 'cash_deposit'
            WHEN 'PREVOD Z UCTU'  THEN 'transfer_in'
            WHEN 'PREVOD NA UCET' THEN 'transfer_out'
            WHEN 'VYBER'          THEN 'cash_withdrawal'
            WHEN 'VYBER KARTOU'   THEN 'card_withdrawal'
            ELSE 'interest_accrual' END                        AS operation,   -- пусто = начисление процентов
       amount::numeric(14,2)           AS amount,
       balance::numeric(14,2)          AS balance_after,
       CASE NULLIF(trim(k_symbol), '')
            WHEN 'SIPO'        THEN 'household'
            WHEN 'UVER'        THEN 'loan_payment'
            WHEN 'SLUZBY'      THEN 'services'
            WHEN 'POJISTNE'    THEN 'insurance'
            WHEN 'UROK'        THEN 'interest'
            WHEN 'SANKC. UROK' THEN 'penalty_interest'
            WHEN 'DUCHOD'      THEN 'pension'
            ELSE NULL END                                      AS purpose,
       NULLIF(trim(bank), '')          AS counterparty_bank,
       NULLIF(trim(account), '')       AS counterparty_account
FROM raw.berka_trans;
ALTER TABLE clean.berka_trans ADD PRIMARY KEY (trans_id);
CREATE INDEX ON clean.berka_trans (account_id, trans_date);