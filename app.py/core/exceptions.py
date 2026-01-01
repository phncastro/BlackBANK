class TransicaoDeEstadoInvalidaError(Exception):
    ''' Exceção lançada quando o Usuário tenta alterar o estado, mas não é permitido.'''

    def __init__(self, *args):
        super().__init__(*args)



class CriacaoDeContaNegadaError(Exception):
    ''' Exceção lançada quando o Banco tenta criar a conta para o usuário mas ele não solicitou,
        ou já está com a conta ativa.'''

    def __init__(self, *args):
        super().__init__(*args)

class EntradaInvalidaError(Exception):
    ''' Exceção lançada quando o usuário tenta inserir um valor que não seja um número.'''

    def __init__(self, *args):
        super().__init__(*args)

class LimiteDepositoError(Exception):
    ''' Exceção lançada quando o usuário tenta depositar um valor, abaixo ou acima
        do limite permitido. '''

    def __init__(self, *args):
        super().__init__(*args)

class LimiteSaqueError(Exception):
    ''' Exceção lançada quando o usuário tenta sacar um valor abaixo do permitido,
        ou um valor acima do saldo disponível.'''

    def __init__(self, *args):
        super().__init__(*args)

class LimiteTransferenciaError(Exception):
    ''' Exceção lançada quando o usuário tenta transferir um valor acima do saldo disponível.'''

    def __init__(self, *args):
        super().__init__(*args)