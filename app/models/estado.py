from sqlalchemy import Integer, DateTime, Enum, Column
from app.database.database import Base
from app.core.status_usuario import StatusUsuario
from datetime import datetime

# Pega a data e hora atual
agora = datetime.now()

# Formata para ANO-MÊS-DIA HORA:MINUTO:SEGUNDO
# %D=Dia, %m=Mês, %Y=Ano, %H=Hora(24h), %M=Minuto, %S=Segundo
data_segundos = agora.strftime("%d-%m-%Y %H:%M:%S")

class Estado(Base):
    __tablename__ = 'estados'
    id = Column(Integer, primary_key=True, index=True)
    estado = Column(Enum(StatusUsuario), nullable=False)
    data_hora = Column(DateTime, default=data_segundos, nullable=False)