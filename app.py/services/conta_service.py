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
        except EntradaInvalidaError:
            raise ValueError('O valor deve ser um número.')

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
        except EntradaInvalidaError:
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
        except EntradaInvalidaError:
            raise EntradaInvalidaError('O valor deve ser um número.')

        if valor <= 0:
            raise LimiteTransferenciaError('O valor deve ser positivo.')
        elif valor > saldo:
            raise LimiteTransferenciaError(f'Você nao possui saldo para esta transferência, seu saldo disponível é de: R${saldo:.2f}.')
        else:
            return True
    
    