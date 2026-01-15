from core.exceptions import EntradaInvalidaError, LimiteDepositoError, LimiteSaqueError, LimiteTransferenciaError

class ContaService:
    ''' Classe que representa os serviços da classe Conta.'''

    @staticmethod
    def regras_de_deposito(valor):
        ''' Método que define as regras para depósito na conta.
        
            Parâmetros:
            
            - valor: Valor a ser filtrado e verificado se é possível fazer o depósito.
            
            Return: Erro, se não for possível, se for autoriza o depósito.
            Define limites de depósito entre R$20,00 e R$15000,00.
        '''
        try:
            valor = float(valor)
        except ValueError:
            raise EntradaInvalidaError('O valor deve ser um número.')

        if valor < 20:
            raise LimiteDepositoError('O depósito mínimo é de R$20,00.')
        elif valor > 15000:
            raise LimiteDepositoError('O depósito máximo é de R$15000,00.')
        else:
            return True      
        
    @staticmethod
    def regras_de_saque(valor, saldo):
        ''' Método que define as regras para saque na conta.
        
            Parâmetros:
            
            - valor: Valor a ser filtrado e verificado se é possível fazer o depósito.
            - saldo: Saldo atual da conta, será consultado para verificar se possui saldo suficiente.
            
            Return: Erro, se não for possível, se for autoriza o saque.
            Define limites de saque entre R$20,00 e o saldo disponível.
        '''
        try:
            valor = float(valor)
        except ValueError:
            raise EntradaInvalidaError('O valor deve ser um número.')

        if valor < 20:
            raise LimiteSaqueError('O saque mínimo é de R$20,00.')
        elif valor > saldo:
            raise LimiteSaqueError(f'Você nao possui saldo para este saque, seu saldo disponível é de: R${saldo:.2f}.')
        else:
            return True
        
    @staticmethod
    def regras_de_transferencia(valor, saldo):
        ''' Método que define as regras para transferência na conta.
        
            Parâmetros:
            
            - Valor: Valor a ser filtrado e verificado se é possível fazer o depósito.
            - saldo: Saldo atual da conta, será consultado para verificar se possui saldo suficiente

            Return: Erro, se não for possível, se for autoriza o depósito.
            Define limites de transfêrencia de no máximo o saldo disponível na conta.
        '''
        try:
            valor = float(valor)
        except ValueError:
            raise EntradaInvalidaError('O valor deve ser um número.')

        if valor <= 0:
            raise LimiteTransferenciaError('O valor deve ser positivo.')
        elif valor > saldo:
            raise LimiteTransferenciaError(f'Você nao possui saldo para esta transferência, seu saldo disponível é de: R${saldo:.2f}.')
        else:
            return True
        
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
    
    