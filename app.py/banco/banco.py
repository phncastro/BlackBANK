from models.usuario import usuarios
from models.conta import Conta

class Banco:

    def criar_conta(usuario):
            if usuario in usuarios and usuario.solicitacao == True:
                conta_user = Conta(usuario._nome, usuario._cpf)
                usuario._status = True


