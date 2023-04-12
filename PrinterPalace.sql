USE PrinterPalace;

# DROP TABLE fff_printer;
# DROP TABLE filament;
#
# DROP TABLE sla_printer;
# DROP TABLE resin;
#
# DROP TABLE printer_model;

CREATE TABLE printer_model(
    model_name VARCHAR(255) PRIMARY KEY,
    brand_name VARCHAR(255),
    printer_type VARCHAR(255),
    bed_width DECIMAL(5, 2),
    bed_length DECIMAL(5, 2),
    bed_height DECIMAL(5, 2)
);

CREATE TABLE filament(
    filament_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    filament_type VARCHAR(255),
    brand_name VARCHAR(255),
    color VARCHAR(255),
    quantity INTEGER
);

CREATE TABLE fff_printer(
    printer_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    printer_name VARCHAR(255) UNIQUE,
    model_name VARCHAR(255),
    current_nozzle_type VARCHAR(255),
    current_nozzle_size DECIMAL(3, 2),
    current_bed_type VARCHAR(255),
    current_filament_id INT,
    FOREIGN KEY (model_name) REFERENCES printer_model(model_name) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (current_filament_id) REFERENCES filament(filament_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE resin(
    resin_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    brand_name VARCHAR(255),
    color VARCHAR(255),
    quantity INTEGER
);

CREATE TABLE sla_printer(
    printer_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    printer_name VARCHAR(255) UNIQUE,
    model_name VARCHAR(255),
    current_resin_id INT,
    FOREIGN KEY (model_name) REFERENCES printer_model(model_name) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (current_resin_id) REFERENCES resin(resin_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO printer_model VALUES("I3 MK3S+", "PRUSA", "FFF", 210.00, 210.00, 250.00);
INSERT INTO printer_model VALUES("MINI+", "PRUSA", "FFF", 180.00, 180.00, 180.00);
INSERT INTO printer_model VALUES("XL", "PRUSA", "FFF", 360.00, 360.00, 360.00);
INSERT INTO printer_model VALUES("SL1S SPEED", "PRUSA", "SLA", 127.00, 80.00, 150.00);

INSERT INTO printer_model VALUES("ENDER 3 PRO", "CREALITY", "FFF", 235.00, 235.00, 235.00);
INSERT INTO printer_model VALUES("ENDER 5", "CREALITY", "FFF", 220.00, 220.00, 300.00);
INSERT INTO printer_model VALUES("CR-10", "CREALITY", "FFF", 300.00, 300.00, 400.00);
INSERT INTO printer_model VALUES("HALOT-ONE PLUS", "CREALITY", "SLA", 172.00, 102.00, 160.00);

INSERT INTO printer_model VALUES("S5 PRO", "ULTIMAKER", "FFF", 300.00, 300.00, 330.00);
INSERT INTO printer_model VALUES("S3", "ULTIMAKER", "FFF", 200.00, 200.00, 250.00);
INSERT INTO printer_model VALUES("2+", "ULTIMAKER", "FFF", 150.00, 150.00, 200.00);

INSERT INTO filament VALUES (10000, "PETG", "PRUSAMENT", "BLACK", 15);
INSERT INTO filament(filament_type, brand_name, color, quantity) VALUES ("PLA", "HATCHBOX", "RED", 24);
INSERT INTO filament(filament_type, brand_name, color, quantity) VALUES ("PLA", "SUNLU", "RED", 24);
INSERT INTO filament(filament_type, brand_name, color, quantity) VALUES ("TPU", "MATTERHACKERS", "BLUE", 3);
INSERT INTO filament(filament_type, brand_name, color, quantity) VALUES ("PLA", "HATCHBOX", "BROWN", 6);
INSERT INTO filament(filament_type, brand_name, color, quantity) VALUES ("PLA", "FORMFUTURA", "BROWN", 12);

INSERT INTO fff_printer VALUES (1000, "YOHAN", "I3 MK3S+", "BRASS", 0.40, "TEXTURED", 10000);
INSERT INTO fff_printer(printer_name, model_name, current_nozzle_type, current_nozzle_size, current_bed_type, current_filament_id) VALUES ("DEBRA", "I3 MK3S+", "BRASS", 0.25, "SMOOTH", 10001);
INSERT INTO fff_printer(printer_name, model_name, current_nozzle_type, current_nozzle_size, current_bed_type, current_filament_id) VALUES ("SMITH", "S5 PRO", "STEEL", 0.25, "TEXTURED", 10002);
INSERT INTO fff_printer(printer_name, model_name, current_nozzle_type, current_nozzle_size, current_bed_type, current_filament_id) VALUES ("EDWIN", "S5 PRO", "BRASS", 0.40, "SMOOTH", 10003);

INSERT INTO resin VALUES (20000, "ANYCUBIC", "RED", 8);
INSERT INTO resin(brand_name, color, quantity) VALUES ("ELEGOO", "BLUE", 12);
INSERT INTO resin(brand_name, color, quantity) VALUES ("PRUSAMENT", "ORANGE", 10);

INSERT INTO sla_printer VALUES (2000, "JOANNE", "HALOT-ONE PLUS", 20000);
INSERT INTO sla_printer(printer_name, model_name, current_resin_id) VALUES ("PRINTER THE CREATOR", "SL1S SPEED", 20002);

CREATE INDEX filament_quantity_idx ON filament (quantity);
CREATE INDEX resin_quantity_idx ON resin (quantity);

CREATE VIEW filament_quantity_by_color AS
SELECT color, SUM(quantity) AS quant
FROM filament
GROUP BY color;

CREATE VIEW filament_quantity_by_type AS
SELECT filament_type, SUM(quantity) AS quant
FROM filament
GROUP BY filament_type;

CREATE VIEW filament_quantity_by_brand AS
SELECT brand_name, SUM(quantity) AS quant
FROM filament
GROUP BY brand_name;


CREATE VIEW resin_quantity_by_color AS
SELECT color, SUM(quantity) AS quant
FROM resin
GROUP BY color;

CREATE VIEW resin_quantity_by_brand AS
SELECT brand_name, SUM(quantity) AS quant
FROM resin
GROUP BY brand_name;


CREATE VIEW all_resin_quantity AS
SELECT brand_name, color, quantity,
       (SELECT SUM(quantity) FROM resin) AS total_quantity
FROM resin;

CREATE VIEW all_filament_quantity AS
SELECT filament_type, brand_name, color, quantity,
       (SELECT SUM(quantity) FROM filament) AS total_quantity
FROM filament;

delimiter $$
CREATE PROCEDURE
sp_getNozzle (
    IN pName VARCHAR(255),
    OUT nozzle VARCHAR(255))
BEGIN
SELECT current_nozzle_type INTO nozzle
FROM fff_printer
WHERE printer_name = pName;
END$$
