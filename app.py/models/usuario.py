from core.status_usuario import StatusUsuario
from core.exceptions import TransicaoDeEstadoInvalidaError

class Usuario:
    ''' Classe Usuario, que representa a pessoa que deseja criar uma conta no Banco. '''
    def __init__(self, nome, cpf):
        ''' Método construtor da class Usuario.
        
            Parâmetros:
            - self: Instância da classe Usuario.
            - nome: Nome do usuário.
            - cpf: CPF do usuário.

            _status: Representa o estado deste usuário, possiveis estados:
            - SEM_CONTA: Valor padrão, quando o usuário ainda não solicitou a criação da conta.
            - SOLICITACAO_PENDENTE: Representa quando o usuário já solicitou a criação da conta.
            - CONTA_ATIVA: Estado final, que representa quando o usuário tem a conta criada.
        '''
        self._nome = nome
        self._cpf = cpf
        self._status = StatusUsuario.SEM_CONTA

    
    def solicitar_criacao_de_conta(self):
        ''' Método que permite ao usuário solicitar a criação da conta.

            Parâmetros:

            - self: Usuário que fez a solicitação

            return: Erro, de acordo com o estado do usuário,
            se o estado atual for SEM_CONTA, permite ele fazer a solicitação,
            alterando assim o estado para SOLICITACAO_PENDENTE.
        '''

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
        ''' Método privado que ativa a conta do usuário.
        
            Parâmetros:
            
            - self: Usuário que terá a conta ativa.

            Return: Erro, se o usuário não puder ter a conta ativa,
            de acordo com o estado atual, se estiver SOLICITACAO_PENDENTE,
            faz a ativação da conta, alterando o estado para CONTA_ATIVA.
        '''
        
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
