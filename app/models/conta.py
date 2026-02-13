from sqlalchemy import Integer, Column, ForeignKey, Float, String, DateTime
from app.database.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Conta(Base):
    '''
    Conta do usuário na instituição financeira Banco,
    '''

# Define a tabela, as colunas e seus tipos
    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String, unique=True, nullable=False, index=True)
    saldo = Column(Float, default=0, nullable=False)
    usuario_id = Column(
        Integer,
        ForeignKey('usuarios.id'),
        unique=True,
        nullable=False)
    usuario = relationship('Usuario', back_populates= 'conta')
    criada_em = Column(DateTime, nullable=False)

# Métodos de Conta

    @staticmethod
    def receber(conta_id, valor):
        '''
        Adiciona saldo a conta
        '''

        conta_id.saldo += valor


    @staticmethod
    def enviar(conta_id, valor):
        '''
        Subtrai valor no saldo da conta
        '''

        conta_id.saldo -= valor





