from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from connection_db import get_db
from models import ObrigacaoAcessoria
from schemas import ObrigacaoAcessoriaCreate, ObrigacaoAcessoriaResponse

router = APIRouter(prefix="/obrigacoes", tags=["Obrigações Acessórias"])


@router.post("/", response_model=ObrigacaoAcessoriaResponse)
def criar_obrigacao(obrigacao: ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    nova_obrigacao = ObrigacaoAcessoria(**obrigacao.model_dump())
    db.add(nova_obrigacao)
    db.commit()
    db.refresh(nova_obrigacao)
    return nova_obrigacao
