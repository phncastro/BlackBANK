from enum import Enum

class TipoTransacao(str, Enum):
    '''
    Enum com as possivéis transações

        - DEPÓSITO
        - SAQUE
        - TRANSFERÊNCIA
    '''

    DEPOSITO = 'depósito'
    SAQUE = 'saque'
    TRANSFERENCIA = 'transferência'
