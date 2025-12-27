class Usuario:
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
    
    def __str__(self):
        return f'Nome: {self._nome.ljust(20)} | CPF: {self._cpf.ljust(20)}'
    
        

    