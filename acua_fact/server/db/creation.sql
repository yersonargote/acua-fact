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

