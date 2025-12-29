
usuarios = []

class Usuario:

    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        self._status = False
        self.solicitacao = False
        usuarios.append(self)


    def __str__(self):
        visual_status = 'Conta ativa' if self._status == True else ('Solicitação pendente' if self.solicitacao == True else 'Usúario sem conta')
        return f'Nome: {self._nome.ljust(20)} | CPF: {self._cpf.ljust(20)} | Status: {visual_status.ljust(20)}'
    
    def solicitar_criacao_de_conta(self):
        self.solicitacao = True

    
        

    