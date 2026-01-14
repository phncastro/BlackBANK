from core.status_usuario import StatusUsuario, Enum
from database.database import Base
from sqlalchemy import Column, Integer, String
from core.status_usuario import StatusUsuario

class Usuario(Base):
    ''' Classe Usuario, que representa a pessoa que deseja criar uma conta no Banco.
        Modelo de sqlachemy '''

    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cpf = Column(Integer, unique= True)
    status = Column(Enum(StatusUsuario))

