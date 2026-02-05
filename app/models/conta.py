from sqlalchemy import Integer, Column, ForeignKey, Float, String
from app.database.database import Base
from sqlalchemy.orm import relationship

class Conta(Base):
    ''' Classe que representa a conta do usuário na instituição financeira Banco.'''

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

    @staticmethod
    def receber(conta_id, valor):
        ''' Método que permite a conta alterar o valor do saldo,
            adicionando o valor de uma transferência. 
            
            parâmetros:

            - valor: Valor que irá ser adicionado no saldo da conta.
        '''
        conta_id.saldo += valor


    @staticmethod
    def enviar(conta_id, valor):
        ''' Método que permite a conta alterar o valor do saldo,
            diminuindo o valor de uma transferência. 
            
            parâmetros:

            - valor: Valor que irá ser debitado no saldo da conta.
        '''
        conta_id.saldo -= valor





