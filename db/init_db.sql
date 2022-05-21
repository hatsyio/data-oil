create schema data_oil_stg;

create table data_oil_stg.provincias
(
    idccaa     text,
    idpovincia text,
    ccaa       text,
    provincia  text
);

create table data_oil_stg.comunidades_autonomas
(
    idccaa text,
    ccaa   text
);

create table data_oil_stg.municipios
(
    idmunicipio text,
    idprovincia text,
    idccaa      text,
    municipio   text,
    provinicia  text,
    ccaa        text
);

create table data_oil_stg.productos_petroliferos
(
    idproducto                text,
    nombreproducto            text,
    nombreproductoabreviatura text
);

create table data_oil_stg.estaciones_terrestres
(
    fecha                              text,
    cp                                 text,
    direccion                          text,
    horario                            text,
    latitud                            text,
    localidad                          text,
    longitud_wgs84                     text,
    margen                             text,
    municipio                          text,
    precio_biodiesel                   text,
    precio_bioetanol                   text,
    precio_gas_natural_comprimido      text,
    precio_gas_natural_licuado         text,
    precio_gases_licuados_del_petróleo text,
    precio_gasoleo_a                   text,
    precio_gasoleo_b                   text,
    precio_gasoleo_premium             text,
    precio_gasolina_95_e10             text,
    precio_gasolina_95_e5              text,
    precio_gasolina_95_e5_premium      text,
    precio_gasolina_98_e10             text,
    precio_gasolina_98_e5              text,
    precio_hidrogeno                   text,
    provincia                          text,
    remision                           text,
    rotulo                             text,
    tipo_venta                         text,
    porcentaje_bioetanol               text,
    porcentaje_ester_metílico          text,
    ideess                             text,
    idmunicipio                        text,
    idprovincia                        text,
    idccaa                             text
);

create schema data_oil_dwh;

create table data_oil_dwh.provincias
(
    idccaa     int,
    idpovincia int,
    ccaa       text,
    provincia  text
);

create table data_oil_dwh.comunidades_autonomas
(
    idccaa int,
    ccaa   text
);

create table data_oil_dwh.municipios
(
    idmunicipio int,
    idprovincia int,
    idccaa      int,
    municipio   text,
    provinicia  text,
    ccaa        text
);

create table data_oil_dwh.productos_petroliferos
(
    idproducto                int,
    nombreproducto            text,
    nombreproductoabreviatura text
);

create table data_oil_dwh.estaciones_terrestres
(
    fecha                              date,
    cp                                 text,
    direccion                          text,
    horario                            text,
    latitud                            text,
    localidad                          text,
    longitud_wgs84                     text,
    margen                             text,
    municipio                          text,
    precio_biodiesel                   text,
    precio_bioetanol                   text,
    precio_gas_natural_comprimido      text,
    precio_gas_natural_licuado         text,
    precio_gases_licuados_del_petróleo text,
    precio_gasoleo_a                   text,
    precio_gasoleo_b                   text,
    precio_gasoleo_premium             text,
    precio_gasolina_95_e10             text,
    precio_gasolina_95_e5              text,
    precio_gasolina_95_e5_premium      text,
    precio_gasolina_98_e10             text,
    precio_gasolina_98_e5              text,
    precio_hidrogeno                   text,
    provincia                          text,
    remision                           text,
    rotulo                             text,
    tipo_venta                         text,
    porcentaje_bioetanol               text,
    porcentaje_ester_metílico          text,
    ideess                             text,
    idmunicipio                        text,
    idprovincia                        text,
    idccaa                             text
);