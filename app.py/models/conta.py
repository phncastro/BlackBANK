from services.conta_service import ContaService
from database.database import Base

class Conta(Base):
    ''' Classe que representa a conta do usuário na instituição financeira Banco.'''

    def __init__(self, usuario, numero_conta):
        '''Construtor da classe Conta.

            parâmetros:

            - usuario: Usuário que vai ter a conta criada.
            - numero_conta: Número único, que pertence a conta deste usuário.
        '''
        self._usuario = usuario
        self._saldo = 0
        self._numero_conta = numero_conta
    
    def depositar(self, valor):
        ''' Método que deposita um valor na conta do usuário.

            Parâmetros:

            - valor: Valor a ser depositado na conta.
        '''
        ContaService.regras_de_deposito(valor)
        self._saldo += valor
        
        return self._saldo

    def sacar(self, valor):
        ''' Método que permite o usuário sacar um valor da conta.

            Parâmetros:

            - valor: Valor do saque desejado.
        '''
        ContaService.regras_de_saque(valor, self._saldo)
        self._saldo -= valor

        return self._saldo

    def transferir(self, conta_destino, valor):
        ''' Método que permite o usuário transferir um valor para outra conta.

            Parâmetros:

            - conta: Conta que irá receber o valor transferido.
            - valor: Valor a ser transferido para a conta desejada.
        '''

        ContaService.regras_de_transferencia(valor, self._saldo)
        self._saldo -= valor
        conta_destino.receber(valor)


    def receber(self, valor):
        ''' Método que permite a conta alterar o valor do saldo,
            adicionando o valor de uma transferência. 
            
            parâmetros:

            - valor: Valor que irá ser adicionado no saldo da conta.
        '''
        self._saldo += valor



