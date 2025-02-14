from fastapi import FastAPI
import routes_empresa
import routes_obrigacao

app = FastAPI()

app.include_router(routes_empresa.router)
app.include_router(routes_obrigacao.router)


@app.get("/")
def read_root():
    return {"message": "API está rodando!"}
