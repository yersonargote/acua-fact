
-- Insert Data in Persona Table

INSERT INTO persona (nombre, direccion, telefono, estrato) VALUES ('Juan', 'Calle 1', '1234567', 1);
INSERT INTO persona (nombre, direccion, telefono, estrato) VALUES ('Pedro', 'Calle 2', '1234567', 2);
INSERT INTO persona (nombre, direccion, telefono, estrato) VALUES ('Maria', 'Calle 3', '1234567', 3);
INSERT INTO persona (nombre, direccion, telefono, estrato) VALUES ('Luis', 'Calle 4', '1234567', 4);

-- Insert Data in Concepto Table
INSERT INTO concepto (nombre, valor, subsidio) VALUES ('Agua', 10000, 0.5);
INSERT INTO concepto (nombre, valor, subsidio) VALUES ('Alcantarillado', 20000, 0.5);
INSERT INTO concepto (nombre, valor, subsidio) VALUES ('Multa', 30000, 0.5);


-- Insert Data in Factura Table
-- INSERT INTO public.factura(fecha_inicio, fecha_fin, fecha_limite_pago, total, persona_id)
-- 	VALUES ('2020-01-01', '2020-01-31', '2020-02-15', 100000, 1);