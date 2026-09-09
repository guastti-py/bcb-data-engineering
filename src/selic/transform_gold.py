import pandas as pd

def transformar_gold(caminho_silver):

    df = pd.read_parquet(caminho_silver)

    df = df.sort_values("data_referencia")

    df_gold = df.groupby(
        ["ano", "mes"]
    )["selic_anual"].agg(
        media="mean",
        minima="min",
        maxima="max",
        primeiro_valor="first",
        ultimo_valor="last",
        quantidade_registros="count"
    ).reset_index()

    df_gold["variacao"] = (
        df_gold["ultimo_valor"]- df_gold["primeiro_valor"]
    )

    caminho_gold = "data/gold/selic_resumo_mensal.parquet"

    df_gold.to_parquet(
        caminho_gold,
        index=False
    )

    print("Transformação Gold concluída")
    
    return caminho_gold

if __name__ == "__main__":
    
    arquivo_gold = transformar_gold(
        "data/silver/selic_historico.parquet"
    )

    print(arquivo_gold)