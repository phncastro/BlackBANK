from sqlalchemy import Integer, Column, Float, Enum, DateTime
from app.database.database import Base
from app.core.transacoes import TipoTransacao

class Transacao(Base):

    __tablename__ = 'transacoes'
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(Enum(TipoTransacao), nullable=False)
    valor = Column(Float)
    id_conta = Column(Integer)
    id_conta_destino = Column(Integer)
    data_hora = Column(DateTime)