# 📌 API de Empresas e Obrigações Acessórias 🚀

Este projeto é uma API construída com **FastAPI**, **SQLAlchemy** e **PostgreSQL** para gerenciar **empresas** e suas **obrigações acessórias**. A API permite criar, listar, atualizar e deletar empresas e obrigações acessórias de forma eficiente.

---

## 📌 Tecnologias Utilizadas

- 🐍 **Python 3.11**
- ⚡ **FastAPI**
- 🗄️ **SQLAlchemy**
- 🐘 **PostgreSQL**
- 🔍 **Pydantic v2**
- 🐳 **Docker e Docker Compose**
- 🔬 **Pytest (para testes unitários)**

---

## 📌 Configuração do Projeto

### 1️⃣ **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/projeto-fastapi.git
cd projeto-fastapi
```

### 2️⃣ **Criação do ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3️⃣ **Instale as dependências**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Configure o arquivo `.env`**
Crie um arquivo `.env` na raiz do projeto e adicione:
```ini
DATABASE_URL=postgresql://admin:admin@localhost:5432/prova_db
```

---

## 📌 Executando o Projeto

### 🔹 **Rodando a API manualmente**
```bash
uvicorn main:app --reload
```
Acesse a documentação Swagger:
📌 **http://127.0.0.1:8000/docs**

---

## 📌 Utilizando Docker

### 🔹 **Subindo o projeto com Docker**
```bash
docker-compose up --build
```
Isso iniciará:
- 🚀 **FastAPI** na porta `8000`
- 🐘 **PostgreSQL** na porta `5432`

---
<!-- ## 📌 Testando a API
## 📌 Testando a API

### 🔹 **Rodar os testes unitários**
```bash
pytest tests/
```

---
-->
## 📌 Endpoints da API

### 🏢 **Empresas**
| Método | Rota             | Descrição |
|--------|----------------|------------|
| **POST**   | `/empresas/`       | Criar uma empresa |
| **GET**    | `/empresas/`       | Listar todas as empresas |
| **GET**    | `/empresas/{id}`   | Buscar empresa por ID |
| **PUT**    | `/empresas/{id}`   | Atualizar empresa |
| **DELETE** | `/empresas/{id}`   | Deletar empresa |

### 📑 **Obrigações Acessórias**
| Método | Rota                | Descrição |
|--------|---------------------|------------|
| **POST**   | `/obrigacoes/`       | Criar uma obrigação acessória |
| **GET**    | `/obrigacoes/`       | Listar todas as obrigações |
| **GET**    | `/obrigacoes/{id}`   | Buscar obrigação por ID |
| **PUT**    | `/obrigacoes/{id}`   | Atualizar obrigação |
| **DELETE** | `/obrigacoes/{id}`   | Deletar obrigação |

---