CREATE TABLE persona (
        nombre VARCHAR NOT NULL,
        direccion VARCHAR NOT NULL,
        telefono VARCHAR NOT NULL,
        estrato INTEGER NOT NULL,
        id SERIAL NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE concepto (
        nombre VARCHAR NOT NULL,
        valor FLOAT NOT NULL,
        subsidio FLOAT NOT NULL,
        id SERIAL NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE factura (
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_limite_pago DATE NOT NULL,
        total FLOAT NOT NULL,
        id SERIAL NOT NULL,
        persona_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(persona_id) REFERENCES persona (id)
);

CREATE TABLE conceptofactura (
        id SERIAL NOT NULL,
        factura_id SERIAL NOT NULL,
        concepto_id SERIAL NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(factura_id) REFERENCES factura (id),
        FOREIGN KEY(concepto_id) REFERENCES concepto (id)
);

CREATE TABLE pago (
        fecha DATE NOT NULL,
        total FLOAT NOT NULL,
        factura_id SERIAL NOT NULL,
        id SERIAL NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(factura_id) REFERENCES factura (id)
);


-- Insert Data in Persona Table

INSERT INTO persona (nombre, direccion, telefono, estrato) VALUES ('Juan', 'Calle 1', '1234567', 1);
INSERT INTO persona (nombre, direccion, telefono, estrato) VALUES ('Pedro', 'Calle 2', '1234567', 2);
INSERT INTO persona (nombre, direccion, telefono, estrato) VALUES ('Maria', 'Calle 3', '1234567', 3);
INSERT INTO persona (nombre, direccion, telefono, estrato) VALUES ('Luis', 'Calle 4', '1234567', 4);

-- Insert Data in Concepto Table
INSERT INTO concepto (nombre, valor, subsidio) VALUES ('Agua', 10000, 0.5);
INSERT INTO concepto (nombre, valor, subsidio) VALUES ('Alcantarillado', 20000, 0.5);
INSERT INTO concepto (nombre, valor, subsidio) VALUES ('Multa', 30000, 0.5);