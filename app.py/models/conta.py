from usuario import Usuario
import random

numeros_de_contas = []

class Conta(Usuario):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self._saldo = 0
        
        while self._numero_conta not in numeros_de_contas:
            
            numero_gerado = random.randint(0, 99999)
            self._numero_conta = str(numero_gerado).zfill(5)

            if self._numero_conta in numeros_de_contas:
                numero_gerado = random.randint(0, 99999)
                self._numero_conta = str(numero_gerado).zfill(5)
                numeros_de_contas.append(self._numero_conta)
            else:
                numeros_de_contas.append(self._numero_conta)

    def __str__(self):
        return f'{super().__str__()} | Nº Conta: {self._numero_conta.ljust(20)} | Saldo: R${self._saldo:.2f}'
    
    def depositar(self):
        while True:
            try:
                valor_deposito = int(input('Qual o valor do depósito? R$'))
            except ValueError:
                print('Digite apenas números')
                continue
            if valor_deposito < 20:
                print('Depósito mínimo é de R$20,00')
            elif valor_deposito > 15000:
                print('Depósito máximo é de R$15000,00')
            else:
                self._saldo += valor_deposito
                print(f'Depósito realizado! Seu novo saldo é de: R${self._saldo:.2f}')
                break

    def sacar(self):
        while True:
            try:
                valor_saque = int(input('Qual o valor do saque? R$'))
            except ValueError:
                print('Digite apenas números')
                continue
            if valor_saque < 20:
                print('Saque mínimo é de R$20,00')
            elif valor_saque > self._saldo:
                print(f'Seu saldo disponível é de: R${self._saldo:.2f}')
            else:
                self._saldo -= valor_saque    
                break


conta1 = Conta('Pablo Henrique', '10492456607')
print(conta1)
conta1.depositar()
print(conta1)
conta1.sacar()
print(conta1)
conta1.sacar()
print(conta1)