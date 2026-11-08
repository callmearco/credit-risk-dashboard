ALTER TABLE clean.berka_account ADD FOREIGN KEY (district_id) REFERENCES clean.berka_district (district_id);
ALTER TABLE clean.berka_client  ADD FOREIGN KEY (district_id) REFERENCES clean.berka_district (district_id);
ALTER TABLE clean.berka_disp    ADD FOREIGN KEY (client_id)   REFERENCES clean.berka_client (client_id),
                                ADD FOREIGN KEY (account_id)  REFERENCES clean.berka_account (account_id);
ALTER TABLE clean.berka_loan    ADD FOREIGN KEY (account_id)  REFERENCES clean.berka_account (account_id),
                                ADD UNIQUE (account_id);
ALTER TABLE clean.berka_order   ADD FOREIGN KEY (account_id)  REFERENCES clean.berka_account (account_id);
ALTER TABLE clean.berka_trans   ADD FOREIGN KEY (account_id)  REFERENCES clean.berka_account (account_id);
ALTER TABLE clean.berka_card    ADD FOREIGN KEY (disp_id)     REFERENCES clean.berka_disp (disp_id);

-- Home Credit: в installments и bureau есть заявки из тестовой выборки, которых нет в application_train — удаляем их перед FK
DELETE FROM clean.hc_installments i WHERE NOT EXISTS (SELECT 1 FROM clean.hc_application a WHERE a.application_id = i.application_id);
DELETE FROM clean.hc_bureau b       WHERE NOT EXISTS (SELECT 1 FROM clean.hc_application a WHERE a.application_id = b.application_id);
ALTER TABLE clean.hc_installments ADD FOREIGN KEY (application_id) REFERENCES clean.hc_application (application_id);
ALTER TABLE clean.hc_bureau       ADD FOREIGN KEY (application_id) REFERENCES clean.hc_application (application_id);