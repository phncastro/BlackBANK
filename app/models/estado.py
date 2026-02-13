from sqlalchemy import Integer, DateTime, Enum, Column
from app.database.database import Base
from app.core.status_usuario import StatusUsuario
from datetime import datetime

class Estado(Base):
    '''
    Mudanças de estado dos usúarios
    '''

# Cria a tabela, suas colunas e seus tipos
    __tablename__ = 'estados'
    id = Column(Integer, primary_key=True, index=True)
    estado_anterior = Column(Enum(StatusUsuario), nullable=False)
    estado_atual = Column(Enum(StatusUsuario), nullable=False)
    data_hora = Column(DateTime, nullable=False)