from connection_db import init_db
from models import Empresa, ObrigacaoAcessoria

if __name__ == "__main__":
    init_db()
    print("📌 Banco de dados criado com sucesso!")
