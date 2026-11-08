DROP TABLE IF EXISTS clean.hc_application CASCADE;
CREATE TABLE clean.hc_application AS
SELECT sk_id_curr::int                                  AS application_id,
       target::int                                      AS is_default,
       name_contract_type                               AS contract_type,
       code_gender                                      AS gender,
       cnt_children::int                                AS children,
       amt_income_total::numeric                        AS income_annual,
       amt_credit::numeric                              AS credit_amount,
       NULLIF(amt_annuity, '')::numeric                 AS annuity,
       name_income_type                                 AS employment_type,
       name_education_type                              AS education,
       name_family_status                               AS family_status,
       (-days_birth::int / 365.25)::int                 AS age_years,
       CASE WHEN days_employed::int > 0 THEN NULL
            ELSE (-days_employed::int / 365.25)::numeric(5,1) END AS employed_years,
       region_rating_client::int                        AS region_rating,
       NULLIF(ext_source_2, '')::numeric                AS score_ext_2,
       NULLIF(ext_source_3, '')::numeric                AS score_ext_3
FROM raw.hc_application;
ALTER TABLE clean.hc_application ADD PRIMARY KEY (application_id);

DROP TABLE IF EXISTS clean.hc_installments CASCADE;
CREATE TABLE clean.hc_installments AS
SELECT sk_id_prev::numeric::bigint                      AS prev_loan_id,
       sk_id_curr::numeric::int                         AS application_id,
       num_instalment_number::numeric::int              AS installment_no,
       days_instalment::numeric::int                    AS days_due,
       NULLIF(days_entry_payment, '')::numeric::int     AS days_paid,
       amt_instalment::numeric                          AS amount_due,
       NULLIF(amt_payment, '')::numeric                 AS amount_paid
FROM raw.hc_installments;
CREATE INDEX ON clean.hc_installments (application_id);

DROP TABLE IF EXISTS clean.hc_bureau CASCADE;
CREATE TABLE clean.hc_bureau AS
SELECT sk_id_bureau::numeric::bigint                    AS bureau_id,
       sk_id_curr::numeric::int                         AS application_id,
       credit_active                                    AS status,
       credit_type,
       days_credit::numeric::int                        AS days_since_open,
       credit_day_overdue::numeric::int                 AS days_overdue,
       NULLIF(amt_credit_sum, '')::numeric              AS credit_amount,
       NULLIF(amt_credit_sum_debt, '')::numeric         AS debt_amount,
       NULLIF(amt_credit_sum_overdue, '')::numeric      AS overdue_amount
FROM raw.hc_bureau;
CREATE INDEX ON clean.hc_bureau (application_id);