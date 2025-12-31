from enum import Enum

class StatusUsuario(Enum):
    SEM_CONTA = 1
    SOLICITACAO_PENDENTE = 2
    CONTA_ATIVA = 3