from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
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


@router.get("/", response_model=List[ObrigacaoAcessoriaResponse])
def listar_obrigacoes(db: Session = Depends(get_db)):
    return db.query(ObrigacaoAcessoria).all()


@router.get("/{obrigacao_id}", response_model=ObrigacaoAcessoriaResponse)
def obter_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    obrigacao = (
        db.query(ObrigacaoAcessoria)
        .filter(ObrigacaoAcessoria.id == obrigacao_id)
        .first()
    )
    if not obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    return obrigacao


@router.put("/{obrigacao_id}", response_model=ObrigacaoAcessoriaResponse)
def atualizar_obrigacao(
    obrigacao_id: int,
    obrigacao_update: ObrigacaoAcessoriaCreate,
    db: Session = Depends(get_db),
):
    obrigacao = (
        db.query(ObrigacaoAcessoria)
        .filter(ObrigacaoAcessoria.id == obrigacao_id)
        .first()
    )
    if not obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")

    for key, value in obrigacao_update.model_dump().items():
        setattr(obrigacao, key, value)

    db.commit()
    db.refresh(obrigacao)
    return obrigacao


@router.delete("/{obrigacao_id}")
def deletar_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    obrigacao = (
        db.query(ObrigacaoAcessoria)
        .filter(ObrigacaoAcessoria.id == obrigacao_id)
        .first()
    )
    if not obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")

    db.delete(obrigacao)
    db.commit()
    return {"message": "Obrigação deletada com sucesso"}
