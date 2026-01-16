from app.core.exceptions import TransicaoDeEstadoInvalidaError
from app.core.status_usuario import StatusUsuario
from app.models.usuario import Usuario

class UsuarioService: 
    ''' Classe que guarda os métodos possiveis da classe Usuario '''

    @staticmethod
    def solicitar_criacao_de_conta(usuario:Usuario):
        ''' Método que permite ao usuário solicitar a criação da conta.

            Parâmetros:

            - usuario: Usuário que fez a solicitação

            return: Erro, se o status do usuário nao for StatusUsuario.SEM_CONTA,
            se o estado atual for SEM_CONTA, permite ele fazer a solicitação,
            alterando assim o estado para SOLICITACAO_PENDENTE.
        '''

        if usuario.status == StatusUsuario.SOLICITACAO_PENDENTE:
            raise TransicaoDeEstadoInvalidaError(
                'Solicitação de criação da conta já está pendente.'
                )
        
        if usuario.status == StatusUsuario.CONTA_ATIVA:
            raise TransicaoDeEstadoInvalidaError(
            'A conta já está ativa.'
            ) 
               
        if usuario.status == StatusUsuario.SEM_CONTA:
            usuario.status = StatusUsuario.SOLICITACAO_PENDENTE
        

    @staticmethod
    def _ativar_conta(usuario:Usuario):
        ''' Método que ativa a conta do usuário quando for aprovada pelo banco.
        
            Parâmetros:
            
            - usuario: Usuário que terá a conta ativa.

            Return: faz a ativação da conta, alterando o estado para CONTA_ATIVA.
        ''' 
               
        if usuario.status == StatusUsuario.SOLICITACAO_PENDENTE:
             usuario.status = StatusUsuario.CONTA_ATIVA


        
