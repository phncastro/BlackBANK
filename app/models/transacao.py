from sqlalchemy import Integer, Column, Float, Enum, DateTime
from app.database.database import Base
from app.core.transacoes import TipoTransacao
from datetime import datetime

class Transacao(Base):
    '''
    Transação feita por Usuários, seja depósito, saque ou transferência
    '''

# Cria a tabela, suas colunas e seus tipos
    __tablename__ = 'transacoes'
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(Enum(TipoTransacao), nullable=False)
    valor = Column(Float)
    num_conta = Column(Integer)
    num_conta_destino = Column(Integer)
    data_hora = Column(DateTime, nullable=False)