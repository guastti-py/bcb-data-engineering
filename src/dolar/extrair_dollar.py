import requests
import json
import os
from datetime import datetime, timedelta

def extrair_dolar():
    
    url = (
    "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
    "CotacaoDolarPeriodo("
    "dataInicial=@dataInicial,"
    "dataFinalCotacao=@dataFinalCotacao"
    ")"
)
    caminho_bronze = "data/bronze/dolar_historico.json"
    
    if os.path.exists(caminho_bronze):
        with open(caminho_bronze, "r", encoding="utf-8") as arquivo:
            dados_antigos = json.load(arquivo)
    else:
        dados_antigos = []
    
    data_inicial = obter_ultima_data_bronze(caminho_bronze)
    data_final = datetime.now().strftime("%m-%d-%Y")
    
    if datetime.strptime(data_inicial, "%m-%d-%Y") > datetime.strptime(data_final, "%m-%d-%Y"):
        print("Nenhum dado novo disponível")
        return caminho_bronze, False

    parametros = {
        "@dataInicial": f"'{data_inicial}'",
        "@dataFinalCotacao": f"'{data_final}'",
        "$format": "json"
    }
    
    resposta = requests.get(url, params=parametros)
    
    dados = resposta.json()
    
    cotacoes = dados["value"]
    
    dados_atualizados = dados_antigos + cotacoes
    
    with open(caminho_bronze, "w", encoding="utf-8") as arquivo:
        json.dump(dados_atualizados, arquivo, ensure_ascii=False, indent=4)
    
    print("Extração do Dólar concluída")
    print("Arquivo Bronze:", caminho_bronze)
    
    return caminho_bronze, True
    

def obter_ultima_data_bronze(caminho_bronze):
    
    if not os.path.exists(caminho_bronze):
        return "01-01-2020"
    
    with open(caminho_bronze, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        
        ultima_data = dados[-1]["dataHoraCotacao"]
        
        ultima_data = datetime.strptime(
            ultima_data,
            "%Y-%m-%d %H:%M:%S.%f"
        )
    
    proxima_data = ultima_data + timedelta(days=1)
    
    return proxima_data.strftime("%m-%d-%Y")

if __name__ == "__main__":
    
    arquivo_bronze, teve_ualizacao = extrair_dolar()
    
    print("Arquivo Bronze:", arquivo_bronze)
    print("Teve atualização:", teve_ualizacao)
    
    