from app.database.database import Base
from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from app.core.status_usuario import StatusUsuario
from datetime import datetime


class Usuario(Base):
    ''' Classe Usuario, que representa a pessoa que deseja criar uma conta no Banco.
        Modelo de sqlalchemy '''

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

