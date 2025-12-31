from core.status_usuario import StatusUsuario
from core.exceptions import TransicaoDeEstadoInvalidaError

class Usuario:

    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        self._status = StatusUsuario.SEM_CONTA

    
    def solicitar_criacao_de_conta(self):

        if self._status == StatusUsuario.SOLICITACAO_PENDENTE:
            raise TransicaoDeEstadoInvalidaError(
                'Solicitação de criação da conta já está pendente.'
                )
        
        if self._status == StatusUsuario.CONTA_ATIVA:
            raise TransicaoDeEstadoInvalidaError(
            'A conta já está ativa.'
            ) 
               
        if self._status == StatusUsuario.SEM_CONTA:
            self._status = StatusUsuario.SOLICITACAO_PENDENTE
        


    def _ativar_conta(self):
        
        if self._status == StatusUsuario.SEM_CONTA:
            raise TransicaoDeEstadoInvalidaError(
                'É preciso solicitar a criação de conta antes de ativá-la'
                )
        
        if self._status == StatusUsuario.CONTA_ATIVA:
            raise TransicaoDeEstadoInvalidaError(
                'Usuário ja está com a conta ativa.'
                ) 
               
        if self._status == StatusUsuario.SOLICITACAO_PENDENTE:
             self._status = StatusUsuario.CONTA_ATIVA
