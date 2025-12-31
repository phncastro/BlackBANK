class TransicaoDeEstadoInvalidaError(Exception):
    ''' Exceção lançada quando o Usuário tenta alterar o estado, mas não é permitido'''

    def __init__(self, *args):
        super().__init__(*args)

class CriacaoDeContaNegadaError(Exception):
    ''' Exceção lançada quando o Banco tenta criar a conta para o usuário mas ele não atende os requisitos'''

    def __init__(self, *args):
        super().__init__(*args)