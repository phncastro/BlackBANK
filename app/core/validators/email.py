from app.core.validators.regex import EMAIL_REGEX
from app.core.exceptions import EmailInvalidoError
import re

dominios_permitidos = [
    'gmail.com',
    'hotmail.com',
    'yahoo.com',
    'outlook.com'
]

def validar_email(email:str):
    '''
        Válida o formato e domínio do CPF -> Email válido
    '''
    if not re.match(EMAIL_REGEX, email):
        raise EmailInvalidoError('Formato de e-mail inválido')
    
    dominio = email.split('@')[-1].lower()

    if dominio not in dominios_permitidos:
        raise EmailInvalidoError('Domínio de e-mail não permitido')
    
    return email