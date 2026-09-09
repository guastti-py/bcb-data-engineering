import pandas as pd

def transformar_silver(caminho_bronze):
    
    df = pd.read_json(caminho_bronze)
    
    df["dataHoraCotacao"] = pd.to_datetime(
        df["dataHoraCotacao"],
        format="%Y-%m-%d %H:%M:%S.%f"
    )
    
    df = df.rename(columns={
        "cotacaoCompra": "cotacao_compra",
        "cotacaoVenda": "cotacao_venda",
        "dataHoraCotacao": "data_cotacao"
    })
    
    df["ano"] = df["data_cotacao"].dt.year
    df["mes"] = df["data_cotacao"].dt.month
    df["day"] = df["data_cotacao"].dt.day
    
    caminho_silver = "data/silver/dolar_historico.parquet"
    
    df.to_parquet(
        caminho_silver,
        index=False
    )
    
    print("Transformação Silver do Dólar concluída")
    
    return caminho_silver

if __name__ == "__main__":
    
    arquivo_silver = transformar_silver(
        "data/bronze/dolar_historico.json"
    )
    
    print("Arquivo Silver:", arquivo_silver)