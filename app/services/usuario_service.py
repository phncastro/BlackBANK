from app.core.exceptions import TransicaoDeEstadoInvalidaError
from app.core.status_usuario import StatusUsuario
from app.models.usuario import Usuario

class UsuarioService: 
    ''' Realiza os serviços possíveis da classe Usuario '''

    @staticmethod
    def solicitar_criacao_de_conta(usuario:Usuario):
        ''' Solicita a criação de conta para o usuário

            Parâmetros:

            - usuario: Usuário que fez a solicitação
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
        ''' Altera o Estado da conta para CONTA_ATIVA quando o banco criar a conta
            para o usuário
        
            Parâmetros:
            
            - usuario: Usuário que teve a conta ativa
        ''' 
               
        if usuario.status == StatusUsuario.SOLICITACAO_PENDENTE:
             usuario.status = StatusUsuario.CONTA_ATIVA


        
