class ContaService:

    def regras_de_deposito(valor):
        try:
            valor = float(valor)
        except ValueError:
            raise ValueError('Erro: O valor deve ser um número.')

        if valor < 20:
            raise ValueError('Erro: O depósito mínimo é de R$20,00.')
        elif valor > 15000:
            raise ValueError('Erro: O depósito máximo é de R$15000,00.')
        else:
            return True      
        
    def regras_de_saque(valor, saldo):
        try:
            valor = float(valor)
        except ValueError:
            raise ValueError('Erro: O valor deve ser um número.')

        if valor < 20:
            raise ValueError('Erro: O saque mínimo é de R$20,00.')
        elif valor > saldo:
            raise ValueError(f'Erro: Você nao possui saldo para este saque, seu saldo disponível é de: R${saldo:.2f}.')
        else:
            return True
        
    def regras_de_transferencia(valor, saldo):
        try:
            valor = float(valor)
        except ValueError:
            raise ValueError('Erro: O valor deve ser um número.')

        if valor <= 0:
            raise ValueError('Erro: O valor deve ser positivo.')
        elif valor > saldo:
            raise ValueError(f'Erro: Você nao possui saldo para esta transferência, seu saldo disponível é de: R${saldo:.2f}.')
        else:
            return True
    
    