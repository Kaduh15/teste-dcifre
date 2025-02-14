from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from connection_db import get_db
from models import Empresa
from schemas import EmpresaCreate, EmpresaResponse

router = APIRouter(prefix="/empresas", tags=["Empresas"])


@router.post("/", response_model=EmpresaResponse)
def criar_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    nova_empresa = Empresa(**empresa.dict())
    db.add(nova_empresa)
    db.commit()
    db.refresh(nova_empresa)
    return nova_empresa
