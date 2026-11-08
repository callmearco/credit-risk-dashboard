DROP TABLE IF EXISTS clean.syn_payment, clean.syn_schedule, clean.syn_loan, clean.syn_client;

CREATE TABLE clean.syn_client (
    client_id int PRIMARY KEY, client_type text NOT NULL, age_years int, gender text,
    income_annual numeric(14,2), employment_type text, family_status text, children int,
    region_id int REFERENCES clean.berka_district (district_id),
    industry_code text REFERENCES clean.ref_industry (industry_code),
    internal_score int, onboarded_date date
);
CREATE TABLE clean.syn_loan (
    loan_id int PRIMARY KEY, client_id int REFERENCES clean.syn_client (client_id),
    product_code text REFERENCES clean.ref_product (product_code), branch_id int,
    channel_code text REFERENCES clean.ref_channel (channel_code),
    currency_code text REFERENCES clean.ref_currency (currency_code),
    original_amount numeric(14,2), term_months int, interest_rate numeric(6,4),
    disbursement_date date, maturity_date date, vintage_month text,
    collateral_type text, collateral_value numeric(14,2),
    is_restructured boolean DEFAULT false, restructured_date date
);
CREATE TABLE clean.syn_schedule (
    loan_id int REFERENCES clean.syn_loan (loan_id), installment_no int, due_date date,
    principal_due numeric(14,2), interest_due numeric(14,2), total_due numeric(14,2),
    PRIMARY KEY (loan_id, installment_no)
);
CREATE TABLE clean.syn_payment (
    loan_id int, installment_no int, paid_date date, amount_paid numeric(14,2),
    PRIMARY KEY (loan_id, installment_no),
    FOREIGN KEY (loan_id, installment_no) REFERENCES clean.syn_schedule (loan_id, installment_no)
);