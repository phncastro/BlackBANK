from services.conta_service import ContaService

class Conta():
    ''' Classe que representa a conta do usuário na instituição financeira Banco.'''

    def __init__(self, usuario, numero_conta):
        '''Construtor da classe Conta.

            parâmetros:

            - self: Instância da classe conta
            - usuario: Usuário que vai ter a conta criada.
            - numero_conta: Número único, que pertence a conta deste usuário.
        '''
        self._usuario = usuario
        self._saldo = 0
        self._numero_conta = numero_conta
    
    def depositar(self, valor):
        ''' Método que deposita um valor na conta do usuário.

            Parâmetros:

            - self: Conta do usuário que será feita o depósito.
            - valor: Valor a ser depositado na conta.
        '''
        deposito_aprovado = ContaService.regras_de_deposito(valor)
        if deposito_aprovado:
            self._saldo += valor
        return self._saldo

    def sacar(self, valor):
        ''' Método que permite o usuário sacar um valor da conta.

            Parâmetros:

            - self: Conta do usuário que será feita o saque.
            - valor: Valor do saque desejado.
        '''
        saque_aprovado = ContaService.regras_de_saque(valor, self._saldo)
        if saque_aprovado:
            self._saldo -= valor

    def transferir(self, conta, valor):
        ''' Método que permite o usuário transferir um valor para outra conta.

            Parâmetros:

            - self: Conta do usuário que será feita a transferência.
            - conta: Conta que irá receber o valor transferido.
            - valor: Valor a ser transferido para a conta desejada.
        '''

        transferencia_aprovada = ContaService.regras_de_transferencia(valor, self._saldo)
        if transferencia_aprovada:
            self._saldo -= valor
            conta.receber(valor)

    def receber(self, valor):
        ''' Método que permite a conta alterar o valor do saldo,
            adicionando o valor de uma transferência. 
            
            parâmetros:

            - self: Conta que irá receber o valor para o seu saldo.
            - valor: Valor que irá ser adicionado no saldo da conta.
        '''
        self._saldo += valor



