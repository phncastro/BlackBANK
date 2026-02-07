from enum import Enum

class TipoTransacao(str, Enum):
    DEPOSITO = 'depósito'
    SAQUE = 'saque'
    TRANSFERENCIA = 'transferência'
