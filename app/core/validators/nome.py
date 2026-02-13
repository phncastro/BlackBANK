import re
from app.core.validators.regex import NOME_REGEX
from app.core.exceptions import NomeInvalidoError

def validar_nome(nome:str):
    '''
        Válida o formato do Nome -> Nome válido    
    '''
    if ' ' not in nome.strip():
        raise NomeInvalidoError('Obrigatório nome e sobrenome')
    
    if not re.match(NOME_REGEX, nome):
        raise NomeInvalidoError('Formato de nome inválido')
    
    return nome
    

