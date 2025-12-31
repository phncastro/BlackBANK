from models.conta import Conta
from models.usuario import Usuario
from random import randint


class Banco:

    def criar_conta(usuario):
        if usuario.status == 'Solicitação pendente':
            conta = Conta(usuario)
            usuario._status = Usuario._ativar_conta()
        numero_gerado = randint(1, 9999)
        conta._numero_conta = str(numero_gerado).zfill(4)

        


            

    


