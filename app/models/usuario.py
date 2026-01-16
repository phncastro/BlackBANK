from app.database.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Usuario(Base):
    ''' Classe Usuario, que representa a pessoa que deseja criar uma conta no Banco.
        Modelo de sqlalchemy '''

    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cpf = Column(Integer, unique= True)
    status = Column(Integer, nullable=False)
    conta = relationship('Conta', back_populates= 'usuario')

