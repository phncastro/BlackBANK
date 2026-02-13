class TransicaoDeEstadoInvalidaError(Exception):
    '''
    Transição de estado não permitida
    '''

    def __init__(self, *args):
        super().__init__(*args)

class CriacaoDeContaNegadaError(Exception):
    '''
    Conta não solicitada pelo Usuário
    '''

    def __init__(self, *args):
        super().__init__(*args)

class EntradaInvalidaError(Exception):
    '''
    Entrada de tipo incorreto
    '''

    def __init__(self, *args):
        super().__init__(*args)

class LimiteDepositoError(Exception):
    '''
    Valor de depósito fora do limite
    '''

    def __init__(self, *args):
        super().__init__(*args)

class LimiteSaqueError(Exception):
    '''
    Valor de saque fora do limite ou saldo
    '''

    def __init__(self, *args):
        super().__init__(*args)

class LimiteTransferenciaError(Exception):
    '''
    Valor excede o limite ou saldo
    '''

    def __init__(self, *args):
        super().__init__(*args)

class CpfInvalidoError(Exception):
    '''
    Formato ou número de CPF inválido
    '''

    def __init__(self, *args):
        super().__init__(*args)

class EmailInvalidoError(Exception):
    '''
    Formato de Email não permitido
    '''

    def __init__(self, *args):
        super().__init__(*args)

class NomeInvalidoError(Exception):
    '''
    Formato de Nome desconhecido ou não aceito
    '''
    
    def __init__(self, *args):
        super().__init__(*args)
