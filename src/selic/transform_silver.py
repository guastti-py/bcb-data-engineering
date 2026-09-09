import pandas as pd

def transformar_silver(caminho_bronze):

    df = pd.read_json(caminho_bronze)

    df["data"] = pd.to_datetime(
        df["data"],
        format="%d/%m/%Y"
    )

    df = df.rename(columns={
        "data": "data_referencia",
        "valor": "selic_anual"
    })
    
    df["selic_anual"] = pd.to_numeric(
        df["selic_anual"],
        errors="coerce"
    )
    
    if df["selic_anual"].isnull().any():
        raise ValueError("Foram encontrados valores nulos na coluna selic_anual")
    
    if df["data_referencia"].duplicated().any():
        raise ValueError("Foram encontradas datas duplicadas na camada Silver")
    

    df["ano"] = df["data_referencia"].dt.year
    df["mes"] = df["data_referencia"].dt.month
    df["dia"] = df["data_referencia"].dt.day

    caminho_silver = "data/silver/selic_historico.parquet"

    df.to_parquet(
        caminho_silver,
        index=False
    )
    
    print("Transformação Silver concluída")
    
    return caminho_silver

if __name__ == "__main__":
    
    arquivo_silver = transformar_silver(
        "data/bronze/selic_historico.json"
    )

    print(arquivo_silver)