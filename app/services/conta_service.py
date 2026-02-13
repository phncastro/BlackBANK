from app.core.exceptions import EntradaInvalidaError, LimiteDepositoError, LimiteSaqueError, LimiteTransferenciaError
from app.models.conta import Conta

class ContaService:
    ''' Realiza os serviços possiveis da classe Conta.'''


    # REGRAS #


    @staticmethod
    def regras_de_deposito(valor):
        ''' Método que define as regras para depósito na conta.
        
            Parâmetros:
            
            - valor: Valor a ser filtrado e verificado se é possível fazer o depósito.
            
            Return: Erro, se não for possível, se for autoriza o depósito.
            Define limites de depósito entre R$20,00 e R$15000,00.
        '''
        try:
            valor = int(valor)
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
        ''' Define as regras para saque na conta.
        
            Parâmetros:
            
            - valor: Valor a ser filtrado e verificado se é possível fazer o saque.
            - saldo: Saldo atual da conta, será consultado para verificar se possui saldo suficiente.
            
            Return: Se for possível autoriza o saque, se não Erro.
            Define limites de saque entre R$20,00 e o saldo disponível.
        '''
        try:
            valor = int(valor)
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
        ''' Define as regras para transferência entre contas.
        
            Parâmetros:
            
            - Valor: Valor a ser filtrado e verificado se é possível fazer a transferência.
            - saldo: Saldo atual da conta, será consultado para verificar se possui saldo suficiente

            Return: Realiza transferência de valor entre contas se possivel, se não Erro.
            Define limite de transfêrencia de no máximo o saldo disponível na conta.
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
    

    # MÉTODOS #


    @staticmethod
    def depositar(conta, valor):
        ''' Deposita um valor na conta do usuário

            Parâmetros:

            - conta: Conta a receber o valor
            - valor: Valor a ser depositado na conta
        '''
        ContaService.regras_de_deposito(valor)
        conta.saldo += valor
        
        return conta.saldo


    @staticmethod
    def sacar(conta, valor):
        ''' Método que permite o usuário sacar um valor da conta

            Parâmetros:

            - conta: Conta a debitar o valor
            - valor: Valor do saque desejado
        '''
        ContaService.regras_de_saque(valor, conta.saldo)
        conta.saldo -= valor

        return conta.saldo
    

    @staticmethod
    def transferir(conta_remetente:Conta,conta_destino:Conta, valor:int):
        ''' Realiza a transferência de saldo, de uma conta para outra

            Parâmetros:

            - conta_remetente: Conta a enviar o valor
            - conta_desitno: Conta que irá receber o valor transferido
            - valor: Valor a ser transferido
        '''

        ContaService.regras_de_transferencia(valor, conta_remetente.saldo)
        conta_remetente.enviar(conta_remetente, valor)
        conta_destino.receber(conta_destino, valor)