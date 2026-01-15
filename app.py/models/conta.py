from sqlalchemy import Integer, Column, ForeignKey
from database.database import Base
from sqlalchemy.orm import relationship

class Conta(Base):
    ''' Classe que representa a conta do usuário na instituição financeira Banco.'''

    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True, index=True)
    numero = Column(Integer)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship('Usuario', back_populates= 'conta')





