import requests
import json
from datetime import datetime, timedelta
import os

def extrair_selic():

    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados"
    
    caminho_bronze = "data/bronze/selic_historico.json"
    
    data_inicial = obter_ultima_data_bronze(caminho_bronze)

    data_final = datetime.now().strftime("%d/%m/%Y")

    parametros = {
        "formato": "json",
        "dataInicial": data_inicial,
        "dataFinal": data_final
    }
    
    if os.path.exists(caminho_bronze):
        with open(caminho_bronze, "r", encoding="utf-8") as arquivo:
            dados_antigos = json.load(arquivo)
    else:
        dados_antigos = []
        
    try:
        
        resposta = requests.get(url, params=parametros, timeout=30)
    
    except requests.exceptions.RequestException as erro:
    
        print("Erro ao acessar a API do Banco Central:")
        print(erro)
    
        return caminho_bronze, False
    
    if resposta.status_code == 404:
        print("Nenhum dados novo disponível")
        return caminho_bronze, False
    
    if resposta.status_code != 200:
        print("Erro na API do Banco Central")
        print("Status:", resposta.status_code)
        
        return caminho_bronze, False
        
    try:
        dados = resposta.json()
    except ValueError:
        print("A resposta da API não veio em JSON válido")
        
        return caminho_bronze, False
    
    if not isinstance(dados, list):
        print("Formato inesperado recebido da API")
        
        return caminho_bronze, False
    
    dados_atualizados = dados_antigos + dados
    
    with open(caminho_bronze, "w", encoding="utf-8") as arquivo:
        json.dump(dados_atualizados, arquivo, ensure_ascii=False, indent=4)
        
    print("Extração da Selic Concluída")
    
    return caminho_bronze, True

def obter_ultima_data_bronze(caminho_bronze):
    
    if not os.path.exists(caminho_bronze):
        return "01/01/2020"
    
    with open(caminho_bronze, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        
    ultima_data = dados[-1]["data"]
    
    ultima_data = datetime.strptime(
        ultima_data,
        "%d/%m/%Y"
    )
    
    proxima_data = ultima_data + timedelta(days=1)
    
    return proxima_data.strftime("%d/%m/%Y")

if __name__ == "__main__":

    arquivo_bronze, teve_atualizacao = extrair_selic()

    print("Arquivo Bronze:", arquivo_bronze)