# 📊 BCB Data Engineering Pipeline

Projeto de Engenharia de Dados desenvolvido para estudo e portfólio utilizando dados públicos do **Banco Central do Brasil**.

O pipeline coleta dados da **Taxa Selic** e do **Dólar PTAX**, realiza tratamento em Python, armazena os dados em PostgreSQL e disponibiliza uma camada analítica em SQL.

---

## 🏗️ Arquitetura

O projeto utiliza uma arquitetura em camadas inspirada no modelo **Medallion**:

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
     Gold - Views
```

### Bronze

Armazena os dados obtidos diretamente das APIs.

```text
data/bronze/selic_historico.json
data/bronze/dolar_historico.json
```

A extração é incremental, buscando apenas dados posteriores à última data armazenada.

### Silver

Realiza limpeza, padronização e tipagem dos dados.

```text
data/silver/selic_historico.parquet
data/silver/dolar_historico.parquet
```

Os dados são armazenados em **Parquet** antes de serem carregados no PostgreSQL.

### Gold

A camada analítica é construída diretamente no PostgreSQL através de Views.

```text
selic_gold
dolar_gold
indicadores_gold
```

As Views calculam indicadores mensais como média, mínimo, máximo, primeiro e último valor e variação.

A `indicadores_gold` reúne Selic e Dólar por ano e mês.

---

## 🔄 Pipeline

O arquivo:

```text
src/main.py
```

orquestra o processo:

```text
API
 ↓
Bronze
 ↓
Silver
 ↓
PostgreSQL
 ↓
Gold
```

As cargas no PostgreSQL utilizam:

```sql
ON CONFLICT (...) DO NOTHING
```

permitindo executar o pipeline várias vezes sem duplicar registros.

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
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🛠️ Tecnologias

- Python
- Pandas
- Requests
- PyArrow
- PostgreSQL
- SQL
- Psycopg
- Git

---

## 🚀 Executando o projeto

Crie e ative o ambiente virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

Crie o banco:

```text
bcb_data_engineering
```

Execute no PostgreSQL:

```text
sql/01_create_tables.sql
sql/02_create_views.sql
```

Crie um arquivo `.env` na raiz:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bcb_data_engineering
DB_USER=postgres
DB_PASSWORD=SUA_SENHA
```

Execute o pipeline:

```powershell
python src\main.py
```

---

## 🌐 Fonte dos dados

Dados públicos disponibilizados pelo **Banco Central do Brasil**.

**Selic:** SGS - Série 1178  
**Dólar:** PTAX - `CotacaoDolarPeriodo`

---

## 📌 Status

🟡 Projeto em desenvolvimento.

Atualmente o pipeline local possui:

```text
Extração incremental
Bronze
Silver
Parquet
PostgreSQL
Gold em SQL
Controle de duplicidade
Versionamento com Git
```

Próxima etapa: evolução do projeto e posterior implementação em **AWS**.