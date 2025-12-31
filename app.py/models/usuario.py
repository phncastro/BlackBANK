class Usuario:

    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        self.status = 'Usuário sem conta'
        '''Adicionar estados permitidos = SEM_CONTA, SOLICITACAO_PENDENTE, CONTA_ATIVA
           não string solta '''
    
    def solicitar_criacao_de_conta(self):
        self.status = 'Solicitação pendente'
        '''Filtrar e limitar o uso da solicitação'''
