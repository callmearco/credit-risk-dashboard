DROP TABLE IF EXISTS raw.berka_account;
CREATE TABLE raw.berka_account (account_id text, district_id text, frequency text, "date" text);

DROP TABLE IF EXISTS raw.berka_client;
CREATE TABLE raw.berka_client (client_id text, gender text, birth_date text, district_id text);

DROP TABLE IF EXISTS raw.berka_disp;
CREATE TABLE raw.berka_disp (disp_id text, client_id text, account_id text, type text);

DROP TABLE IF EXISTS raw.berka_district;
CREATE TABLE raw.berka_district (district_id text, a2 text, a3 text, a4 text, a5 text, a6 text, a7 text,
    a8 text, a9 text, a10 text, a11 text, a12 text, a13 text, a14 text, a15 text, a16 text);

DROP TABLE IF EXISTS raw.berka_loan;
CREATE TABLE raw.berka_loan (loan_id text, account_id text, "date" text, amount text, duration text,
    payments text, status text);

DROP TABLE IF EXISTS raw.berka_order;
CREATE TABLE raw.berka_order (order_id text, account_id text, bank_to text, account_to text, amount text,
    k_symbol text);

DROP TABLE IF EXISTS raw.berka_trans;
CREATE TABLE raw.berka_trans (trans_id text, account_id text, "date" text, type text, operation text,
    amount text, balance text, k_symbol text, bank text, account text);

DROP TABLE IF EXISTS raw.berka_card;
CREATE TABLE raw.berka_card (card_id text, disp_id text, type text, issued text);

DROP TABLE IF EXISTS raw.hc_installments;
CREATE TABLE raw.hc_installments (sk_id_prev text, sk_id_curr text, num_instalment_version text,
    num_instalment_number text, days_instalment text, days_entry_payment text, amt_instalment text,
    amt_payment text);

DROP TABLE IF EXISTS raw.hc_bureau;
CREATE TABLE raw.hc_bureau (sk_id_curr text, sk_id_bureau text, credit_active text, credit_currency text,
    days_credit text, credit_day_overdue text, days_credit_enddate text, days_enddate_fact text,
    amt_credit_max_overdue text, cnt_credit_prolong text, amt_credit_sum text, amt_credit_sum_debt text,
    amt_credit_sum_limit text, amt_credit_sum_overdue text, credit_type text, days_credit_update text,
    amt_annuity text);

-- raw.hc_application: 122 колонки — вставь вывод скрипта ниже