# ETL Pipeline

Projeto desenvolvido durante estudos de arquitetura de ETL (Extract, Transform and Load), utilizando Python, testes automatizados, integração com banco de dados MySQL e aplicação de boas práticas como contratos, interfaces, linting e validações.

---

## 📌 Objetivo

O projeto tem como objetivo:

- Extrair dados de uma página HTML
- Transformar os dados em um formato padronizado
- Carregar os dados em um banco MySQL
- Aplicar arquitetura desacoplada e escalável
- Garantir qualidade através de testes unitários e lint

---

# 🏗️ Arquitetura do Projeto

A estrutura foi organizada seguindo responsabilidades bem definidas entre camadas:

```bash
ETL/
│
├── src/
│   ├── drivers/
│   │   ├── interfaces/
│   │   ├── mocks/
│   │   └── tests/
│   │
│   ├── errors/
│   │
│   ├── infra/
│   │   ├── interfaces/
│   │   └── __pycache__/
│   │
│   ├── main/
│   │
│   ├── stages/
│   │   ├── contracts/
│   │   │   └── mocks/
│   │   │
│   │   ├── extract/
│   │   ├── transform/
│   │   └── load/
│
├── venv/
├── db.sql
├── requirements.txt
├── run.py
└── .env
```

---

# 🔄 Fluxo do Pipeline

O pipeline segue o fluxo clássico de ETL:

```text
Extração → Transformação → Carregamento
```

## 1️⃣ Extract

Responsável por:

- Fazer requisições HTTP
- Coletar HTML
- Buscar os dados brutos

Arquivos principais:

- `http_requester.py`
- `html_collector.py`
- `extract_html.py`

---

## 2️⃣ Transform

Responsável por:

- Limpar os dados
- Estruturar informações
- Validar formato
- Criar contratos de transferência entre etapas

Arquivo principal:

- `transform_raw_data.py`

---

## 3️⃣ Load

Responsável por:

- Inserir dados transformados no banco MySQL
- Persistir informações

Arquivos principais:

- `load.py`
- `database_repository.py`
- `database_connector.py`

---

# 📦 Contratos

O projeto utiliza contratos para padronizar a comunicação entre os estágios do ETL.

Benefícios:

- Imutabilidade
- Segurança na transferência de dados
- Desacoplamento entre etapas
- Melhor manutenção

---

# 🧪 Testes

Foram implementados testes unitários utilizando:

- `pytest`

Exemplos:

- Testes de extração
- Testes de transformação
- Testes de carregamento
- Repositórios mockados
- Simulação de erros

Executar testes:

```bash
python -m pytest -s -v
```

---

# ✅ Qualidade de Código

Ferramentas utilizadas:

- `pylint`
- `pre-commit`

Verificar lint:

```bash
pylint src
```

---

# 🗄️ Banco de Dados

Banco utilizado:

- MySQL

Script SQL:

```bash
db.sql
```

Conexão realizada via:

```python
mysql.connector
```

---

# ⚙️ Configuração do Projeto

## Criar ambiente virtual

```bash
python3 -m venv venv
```

## Ativar ambiente

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

# 📥 Instalar dependências

```bash
pip install -r requirements.txt
```

---

# 🔐 Variáveis de Ambiente

Criar arquivo `.env`:

```env
passwd=SUA_SENHA_MYSQL
```

---

# ▶️ Executar Projeto

```bash
python3 run.py
```

---

# 🛠️ Tecnologias Utilizadas

- Python 3.12
- Pytest
- Pylint
- MySQL
- BeautifulSoup4
- Requests
- Pre-commit

---

# 📚 Conceitos Aplicados

- ETL Pipeline
- Clean Architecture
- Repository Pattern
- Contracts
- Interfaces
- Dependency Injection
- Testes Unitários
- Tratamento de erros
- Linting

---

# 👩‍💻 Autora

Rafaela Brícia  
Projeto desenvolvido para fins de estudo e prática de arquitetura ETL com Python.
