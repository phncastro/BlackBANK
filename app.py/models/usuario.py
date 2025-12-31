from core.status_usuario import StatusUsuario
from core.exceptions import TransicaoDeEstadoInvalidaError

class Usuario:

    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        self._status = StatusUsuario.SEM_CONTA

    
    def solicitar_criacao_de_conta(self):
        if self._status == StatusUsuario.SOLICITACAO_PENDENTE:
            raise TransicaoDeEstadoInvalidaError('Não é possível alterar para o mesmo estado.')
        
        elif self._status == StatusUsuario.CONTA_ATIVA:
            raise TransicaoDeEstadoInvalidaError('Não é possível alterar o estado com a conta ativa.') 
               
        else:
            self._status = StatusUsuario.SOLICITACAO_PENDENTE
        


    def _ativar_conta(self):
        '''Verificar se o status atual permite ativação
           lançar erro se não permitir
           mudar o Enum'''
        
        if self._status == StatusUsuario.SEM_CONTA:
            raise TransicaoDeEstadoInvalidaError('É preciso solicitar a criação de conta antes de ativá-la')
        
        elif self._status == StatusUsuario.CONTA_ATIVA:
            raise TransicaoDeEstadoInvalidaError('Usuário ja está com a conta ativa.') 
               
        else:
             self._status = StatusUsuario.CONTA_ATIVA
