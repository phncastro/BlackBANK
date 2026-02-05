from enum import Enum

class Transacoes(str, Enum):
    DEPOSITO = 'depósito'
    SAQUE = 'saque'
    TRANSFERENCIA = 'transferência'
