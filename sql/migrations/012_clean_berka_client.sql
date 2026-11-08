DROP TABLE IF EXISTS clean.berka_client CASCADE;
CREATE TABLE clean.berka_client AS
SELECT client_id::int AS client_id, gender, birth_date::date AS birth_date, district_id::int AS district_id
FROM raw.berka_client;
ALTER TABLE clean.berka_client ADD PRIMARY KEY (client_id);