from selic.teste_api import extrair_selic
from selic.transform_silver import transformar_silver
from selic.transform_gold import transformar_gold
from dolar.extrair_dollar import extrair_dolar
from dolar.transform_silver import transformar_silver as transformar_silver_dolar
from dolar.transform_gold import transformar_gold as transformar_gold_dolar

arquivo_bronze, teve_atualizacao = extrair_selic()

if teve_atualizacao:
    arquivo_silver = transformar_silver(arquivo_bronze)

    arquivo_gold = transformar_gold(arquivo_silver)

    print("Pipeline concluído com sucesso")
    print(arquivo_gold)
else:
    print("Pipeline encerrado: não há novos dados para processar.")
    
arquivo_bronze_dolar, teve_atualizacao_dolar = extrair_dolar()
    
if teve_atualizacao_dolar:
    
    arquivo_silver_dolar = transformar_silver_dolar(
        arquivo_bronze_dolar
    )
    
    arquivo_gold_dolar = transformar_gold_dolar(
        arquivo_silver_dolar
    )
    
    print("Pipeline do Dólar concluído com sucesso")
    print(arquivo_gold_dolar)

else:
    
    print("Pipeline do Dólar encerrado: não há novos dados para processar.")