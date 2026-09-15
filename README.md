# 📊 BCB Data Engineering Pipeline

Pipeline de Engenharia de Dados desenvolvido com **Python, PostgreSQL e dados públicos do Banco Central do Brasil**.

O projeto coleta dados históricos da **Taxa Selic** e do **Dólar PTAX**, realiza tratamento e padronização dos dados e disponibiliza uma camada analítica no PostgreSQL.

---

## 🎯 Objetivo

O objetivo deste projeto foi praticar os principais fundamentos de um pipeline de Engenharia de Dados:

- consumo de APIs;
- extração incremental;
- transformação de dados;
- armazenamento em JSON e Parquet;
- carga em banco de dados;
- modelagem em camadas Bronze, Silver e Gold;
- SQL para criação de indicadores;
- versionamento com Git e GitHub.

---

## 🏗️ Arquitetura

```text
Banco Central do Brasil
          ↓
        APIs
          ↓
       Python
          ↓
   Bronze - JSON
          ↓
  Silver - Parquet
          ↓
     PostgreSQL
          ↓
    Gold - SQL Views
```

### 🥉 Bronze

Armazena os dados obtidos das APIs em seu formato mais próximo da origem.

```text
data/bronze/
```

### 🥈 Silver

Realiza limpeza, conversão de tipos e padronização dos dados.

Os arquivos tratados são armazenados em formato **Parquet**.

```text
data/silver/
```

### 🥇 Gold

A camada analítica é construída diretamente no PostgreSQL através de Views.

```text
selic_gold
dolar_gold
indicadores_gold
```

São calculados indicadores mensais como:

- média;
- mínimo;
- máximo;
- primeiro valor do mês;
- último valor do mês;
- quantidade de registros;
- variação mensal.

A `indicadores_gold` consolida Selic e Dólar por ano e mês.

---

## 🔄 Carga incremental

O pipeline verifica a última data já armazenada antes de consultar novamente as APIs.

Dessa forma, apenas novos dados são buscados.

Na carga para o PostgreSQL é utilizado:

```sql
ON CONFLICT (...) DO NOTHING
```

evitando registros duplicados.

---

## 📂 Estrutura

```text
bcb-data-engineering/
│
├── data/
│   ├── bronze/
│   └── silver/
│
├── sql/
│   ├── 01_create_tables.sql
│   └── 02_create_views.sql
│
├── src/
│   ├── database/
│   ├── dolar/
│   ├── selic/
│   └── main.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🛠️ Tecnologias

`Python` • `Pandas` • `Requests` • `PyArrow` • `PostgreSQL` • `SQL` • `Psycopg` • `Git` • `GitHub`

---

## 🚀 Executando o projeto

Crie o ambiente virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

Crie um arquivo `.env` utilizando o `.env.example` como referência.

No PostgreSQL, execute:

```text
sql/01_create_tables.sql
sql/02_create_views.sql
```

Depois execute:

```powershell
python src\main.py
```

---

## 🌐 Fonte dos dados

Dados públicos disponibilizados pelo **Banco Central do Brasil**.

**Selic:** SGS - Série 1178  
**Dólar:** PTAX

---

## 📌 Status

✅ Pipeline local funcionando.

Próximas evoluções planejadas:

```text
Orquestração
AWS
Automação em nuvem
```

---

## 📚 Sobre o projeto

Este projeto faz parte do meu processo de aprendizado e transição para a área de **Dados / Engenharia de Dados**.

O foco foi construir o pipeline passo a passo e entender a responsabilidade de cada camada e tecnologia utilizada.