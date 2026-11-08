DROP TABLE IF EXISTS clean.ref_bucket CASCADE;
CREATE TABLE clean.ref_bucket (bucket_code text PRIMARY KEY, bucket_order int, dpd_from int, dpd_to int);
INSERT INTO clean.ref_bucket VALUES ('0',1,0,0), ('1-30',2,1,30), ('31-60',3,31,60), ('61-90',4,61,90), ('90+',5,91,100000);

DROP TABLE IF EXISTS clean.ref_product CASCADE;
CREATE TABLE clean.ref_product (product_id int PRIMARY KEY, product_code text UNIQUE, product_name text,
    product_group text, risk_class text, default_currency text, lgd numeric(4,2));
INSERT INTO clean.ref_product VALUES
    (1,'consumer','Consumer loan','loan','high','KGS',0.45),
    (2,'auto','Auto loan','loan','medium','KGS',0.25),
    (3,'sme','SME term loan','loan','medium','KGS',0.35);

DROP TABLE IF EXISTS clean.ref_channel CASCADE;
CREATE TABLE clean.ref_channel (channel_code text PRIMARY KEY, channel_name text);
INSERT INTO clean.ref_channel VALUES ('branch','Branch'), ('online','Online'), ('partner','Partner / dealer');

DROP TABLE IF EXISTS clean.ref_industry CASCADE;
CREATE TABLE clean.ref_industry (industry_code text PRIMARY KEY, industry_name text);
INSERT INTO clean.ref_industry VALUES ('trade','Trade'), ('construction','Construction'), ('agri','Agriculture'),
    ('manufacturing','Manufacturing'), ('transport','Transport & logistics'), ('services','Other services'), ('it','IT & telecom');

DROP TABLE IF EXISTS clean.ref_currency CASCADE;
CREATE TABLE clean.ref_currency (currency_code text PRIMARY KEY, currency_name text);
INSERT INTO clean.ref_currency VALUES ('KGS','Kyrgyz som'), ('USD','US dollar'), ('EUR','Euro'), ('RUB','Russian rouble');