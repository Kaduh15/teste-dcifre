from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database_base import Base


class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)
    endereco = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefone = Column(String, nullable=False)

    obrigacoes = relationship(
        "ObrigacaoAcessoria", back_populates="empresa", cascade="all, delete"
    )


class ObrigacaoAcessoria(Base):
    __tablename__ = "obrigacoes_acessorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    periodicidade = Column(String, nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresas.id", ondelete="CASCADE"))

    empresa = relationship("Empresa", back_populates="obrigacoes")
