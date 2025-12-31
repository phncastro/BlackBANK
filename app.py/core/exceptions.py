class TransicaoDeEstadoInvalidaError(Exception):
    ''' Exceção lançada quando Usuário tenta alterar o estado, mas não é permitido'''

    def __init__(self, *args):
        super().__init__(*args)