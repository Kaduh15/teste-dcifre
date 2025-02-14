from fastapi import FastAPI
from config import settings
import routes_empresa
import routes_obrigacao

app = FastAPI()

app.include_router(routes_empresa.router)
app.include_router(routes_obrigacao.router)


@app.get("/")
def read_root():
    return {
        f"message": "API está rodando! acesse a documentação em /docs",
        "link": f"{settings.DEPLOY_URL or 'http://localhost:8000'}/docs",
    }
