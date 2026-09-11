import os 

import pandas as pd
import psycopg
from dotenv import load_dotenv

load_dotenv()

def carregar_dolar_silver(caminho_silver):

    df = pd.read_parquet(caminho_silver)

    print("Colunas encconradas:")
    print(df.columns)

    print()
    print("Quantidade de registros:", len(df))

    conexao = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
        
    )

    cursor = conexao.cursor()

    sql = """
    INSERT INTO dolar_silver (
        cotacao_compra,
        cotacao_venda,
        data_cotacao,
        ano,
        mes,
        dia
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (data_cotacao)
    DO NOTHING;
    """

    registros = list(
        df[
            [
                "cotacao_compra",
                "cotacao_venda",
                "data_cotacao",
                "ano",
                "mes",
                "dia"
            ]
        ].itertuples(
            index=False,
            name=None
        )
    )

    cursor.executemany(
        sql,
        registros
    )

    conexao.commit()

    print()
    print("Silver do Dólar carregada no PostgreSQL com sucesso!")
    print("Registros processados:", len(registros))

    cursor.close()
    conexao.close()
    
if __name__ == "__main__":
    
    carregar_dolar_silver(
        "data/silver/dolar_historico.parquet"
    )