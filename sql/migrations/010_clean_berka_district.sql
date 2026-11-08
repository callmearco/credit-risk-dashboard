DROP TABLE IF EXISTS clean.berka_district CASCADE;
CREATE TABLE clean.berka_district AS
SELECT district_id::int AS district_id,
        a2              AS district_name,
        a3              AS region_name,
        a4::int         AS inhabitants,
        a10::numeric    AS urban_ratio_pct,
        a11::int        AS avg_salary,
        NULLIF(a12, '?')::numeric AS unemployment_95,
        a13::numeric    AS unemployment_96,
       a14::int                      AS entrepreneurs_per_1000,
        NULLIF(a15, '?')::int AS crimes_95,
        a16::int        AS crimes_96
FROM raw.berka_district;
ALTER TABLE clean.berka_district ADD PRIMARY KEY (district_id);