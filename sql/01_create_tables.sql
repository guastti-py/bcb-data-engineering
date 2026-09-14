CREATE TABLE IF NOT EXISTS seic_silver (

data_referencia DATE PRIMARY KEY,
selic_anual DOUBLE PRECISION,
ano INTEGER,
mes INTEGER,
dia INTEGER
);

CREATE TABLE IF NOT EXISTS dolar_silver(

cotacao_compra DOUBLE PRECISION,
cotacao_venda DOUBLE PRECISION,
data_cotacao TIMESTAMP PRIMARY KEY,
ano INTEGER,
mes INTEGER,
dia INTEGER
);

