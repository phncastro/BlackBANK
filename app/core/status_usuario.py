from enum import Enum

class StatusUsuario(str, Enum):
    '''Enum para guardar os possíveis estados do Usuário

        - SEM_CONTA = Valor que vem por padrão,
        representa quando o usuário ainda não solicitou a criação da conta,
        e não possui conta ativa

        - SOLICITAÇAO_PENDENTE = Estado que representa quando o usuário já solicitou a criação da conta,
          mas não foi aceita ainda.

        - CONTA_ATIVA = Estado final, que demonstra que o usuário já possui a conta ativa.
        
        '''
    SEM_CONTA = "SEM_CONTA"
    SOLICITACAO_PENDENTE = "SOLICITACAO_PENDENTE"
    CONTA_ATIVA = "CONTA_ATIVA"