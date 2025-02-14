from pydantic import BaseModel, EmailStr
from typing import List, Literal


class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: Literal["mensal", "trimestral", "anual"]
    empresa_id: int


class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    pass


class ObrigacaoAcessoriaResponse(ObrigacaoAcessoriaBase):
    id: int

    class Config:
        from_attributes = True


class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: EmailStr
    telefone: str


class EmpresaCreate(EmpresaBase):
    pass


class EmpresaResponse(EmpresaBase):
    id: int
    obrigacoes: List[ObrigacaoAcessoriaResponse] = []

    class Config:
        from_attributes = True
