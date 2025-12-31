from services.contaService import ContaService

class Conta():

    def __init__(self, usuario, numero_conta):
        self._usuario = usuario
        self._saldo = 0
        self._numero_conta = numero_conta
    
    def depositar(self, valor):
        deposito_aprovado = ContaService.regras_de_deposito(valor)
        if deposito_aprovado:
            self._saldo += valor

    def sacar(self, valor):
        saque_aprovado = ContaService.regras_de_saque(valor, self._saldo)
        if saque_aprovado:
            self._saldo -= valor

    def transferir(self, conta, valor):
        transferencia_aprovada = ContaService.regras_de_transferencia(valor, self._saldo)
        if transferencia_aprovada:
            self._saldo -= valor
            conta.receber(valor)

    def receber(self, valor):
        self._saldo += valor



