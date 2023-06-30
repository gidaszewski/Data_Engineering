create table if not exists francogidaszewski_coderhouse.tipo_de_cambio (
    id INT NOT NULL,
    fecha DATE distkey,
    tipo_de_cambio decimal(10,2),
    tasa_politica_monetaria decimal(10,2)
) sortkey(fecha);

ALTER TABLE ALTER franco_gidaszewski.tipo_de_cambio SORTKEY AUTO;