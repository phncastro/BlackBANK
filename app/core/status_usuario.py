from enum import Enum

class StatusUsuario(str, Enum):
    '''
    Enum com os possíveis estados do Usuário

      - SEM_CONTA = Valor inicial de Usuário

      - SOLICITAÇAO_PENDENTE = Conta solicitada

      - CONTA_ATIVA = Conta de Usuário ativa
    '''

    SEM_CONTA = "SEM_CONTA"
    SOLICITACAO_PENDENTE = "SOLICITACAO_PENDENTE"
    CONTA_ATIVA = "CONTA_ATIVA"