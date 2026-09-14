CREATE OR REPLACE VIEW selic_gold AS

SELECT
    ano,
    mes,
    ROUND(AVG(selic_anual)::numeric, 2 ) AS media,
    ROUND(MIN(selic_anual)::numeric, 2 ) AS minima,
    ROUND(MAX(selic_anual)::numeric, 2 ) AS maxima,
    ROUND((ARRAY_AGG(selic_anual ORDER BY data_referencia))[1]::numeric, 2 ) AS primeiro_valor,
    ROUND((ARRAY_AGG(selic_anual ORDER BY data_referencia DESC))[1]::numeric, 2 ) AS ultimo_valor,
    COUNT(*) AS quantidade_registros,
    ROUND(((ARRAY_AGG(selic_anual ORDER BY data_referencia DESC))[1]
        -  (ARRAY_AGG(selic_anual ORDER BY data_referencia))[1])::numeric, 2 ) AS variacao
FROM selic_silver
GROUP BY ano, mes;


CREATE OR REPLACE VIEW dolar_gold AS

SELECT
    ano,
    mes,
    ROUND(AVG(cotacao_venda)::numeric, 2 ) AS media,
    ROUND(MIN(cotacao_venda)::numeric, 2 ) AS minima,
    ROUND(MAX(cotacao_venda)::numeric, 2 ) AS maxima,
    ROUND((ARRAY_AGG(cotacao_venda ORDER BY data_cotacao))[1]::numeric, 2 ) AS primeiro_valor,
    ROUND((ARRAY_AGG(cotacao_venda ORDER BY data_cotacao DESC))[1]::numeric, 2 ) AS ultimo_valor,
    COUNT(*) AS quantidade_registros,
    ROUND(((ARRAY_AGG(cotacao_venda ORDER BY data_cotacao DESC))[1]
    -      (ARRAY_AGG(cotacao_venda ORDER BY data_cotacao))[1])::numeric, 2 ) AS variacao
FROM dolar_silver
GROUP BY ano, mes;


CREATE OR REPLACE VIEW indicadores_gold AS

SELECT
    s.ano,
    s.mes,

    s.media AS selic_media,
    s.minima AS selic_minima,
    s.maxima AS selic_maxima,
    s.primeiro_valor AS selic_primeiro_valor,
    s.ultimo_valor AS selic_ultimo_valor,
    s.variacao AS selic_variacao,

    d.media AS dolar_media,
    d.minima AS dolar_minima,
    d.maxima AS dolar_maxima,
    d.primeiro_valor AS dolar_primeiro_valor,
    d.ultimo_valor AS dolar_ultimo_valor,
    d.variacao AS dolar_variacao

FROM selic_gold s

INNER JOIN dolar_gold d
    ON s.ano = d.ano
   AND s.mes = d.mes;