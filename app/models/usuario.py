from app.database.database import Base
from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from app.core.status_usuario import StatusUsuario
from datetime import datetime


class Usuario(Base):
    '''
    Pessoa que deseja possuir conta no Banco
    '''

# Cria a tabela, suas colunas e seus tipos
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique= True)
    email = Column(String, unique=True)
    status = Column(Enum(StatusUsuario), nullable=False, default=StatusUsuario.SEM_CONTA)
    conta = relationship(
        'Conta',
        back_populates= 'usuario',
        uselist=False,
        cascade="all, delete")
    criado_em = Column(DateTime, nullable=False)

