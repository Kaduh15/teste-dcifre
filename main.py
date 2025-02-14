from fastapi import FastAPI
import routes_empresa

app = FastAPI()

app.include_router(routes_empresa.router)

@app.get("/")
def read_root():
    return {"message": "API está rodando!"}
