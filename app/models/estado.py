from sqlalchemy import Integer, DateTime, Enum, Column
from app.database.database import Base
from app.core.status_usuario import StatusUsuario
from datetime import datetime

class Estado(Base):
    __tablename__ = 'estados'
    id = Column(Integer, primary_key=True, index=True)
    estado = Column(Enum(StatusUsuario), nullable=False)
    data_hora = Column(DateTime, nullable=False)