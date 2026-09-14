from selic.teste_api import extrair_selic
from selic.transform_silver import transformar_silver

from dolar.extrair_dollar import extrair_dolar
from dolar.transform_silver import transformar_silver as transformar_silver_dolar

from database.carregar_selic_silver import carregar_selic_silver
from database.carregar_dolar_silver import carregar_dolar_silver


# =========================
# SELIC
# =========================

arquivo_bronze, teve_atualizacao = extrair_selic()

if teve_atualizacao:

    arquivo_silver = transformar_silver(
        arquivo_bronze
    )

else:

    print(
        "Selic sem novos dados. "
        "Utilizando a Silver existente."
    )

    arquivo_silver = "data/silver/selic_historico.parquet"


carregar_selic_silver(
    arquivo_silver
)

print("Pipeline da Selic concluído com sucesso")
print(arquivo_silver)


# =========================
# DÓLAR
# =========================

arquivo_bronze_dolar, teve_atualizacao_dolar = extrair_dolar()

if teve_atualizacao_dolar:

    arquivo_silver_dolar = transformar_silver_dolar(
        arquivo_bronze_dolar
    )

else:

    print(
        "Dólar sem novos dados. "
        "Utilizando a Silver existente."
    )

    arquivo_silver_dolar = "data/silver/dolar_historico.parquet"


carregar_dolar_silver(
    arquivo_silver_dolar
)

print("Pipeline do Dólar concluído com sucesso")
print(arquivo_silver_dolar)