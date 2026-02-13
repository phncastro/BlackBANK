import re
from app.core.exceptions import CpfInvalidoError
from app.core.validators.regex import CPF_REGEX

def validar_cpf(cpf:str):
    '''
        Válida o formato e tamanho do CPF -> CPF válido   
    '''
    cpf = re.sub(r'[.-]', '', cpf)

    if not re.match(CPF_REGEX, cpf):
        raise CpfInvalidoError('CPF deve conter exatamente 11 dígitos')
    
    if (cpf[0] * 11) == cpf:
        raise CpfInvalidoError('CPF inválido')

    def calcula_digito(cpf, multiplicador):
        soma = sum(int(cpf[i]) * (multiplicador - i) for i in range(multiplicador - 1))
        resto = (soma * 10) % 11
        return 0 if resto == 10 else resto

    if calcula_digito(cpf, 10) != int(cpf[9]) or calcula_digito(cpf, 11) != int(cpf[10]):
        raise CpfInvalidoError('CPF inválido')
    
    return cpf

