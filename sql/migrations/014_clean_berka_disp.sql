DROP TABLE IF EXISTS clean.berka_disp CASCADE;
CREATE TABLE clean.berka_disp AS
SELECT disp_id::int AS disp_id, client_id::int AS client_id, account_id::int AS account_id, lower(type) AS role
FROM raw.berka_disp;
ALTER TABLE clean.berka_disp ADD PRIMARY KEY (disp_id); 