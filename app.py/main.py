from models.usuario import Usuario
from models.banco import Banco

user1 = Usuario('Pablo', '10492456607')
user2 = Usuario('Joao', '01234567891')
user3 = Usuario('Claudio', '05242351758')

banco = Banco()

print(user1)
user1.solicitar_criacao_de_conta()
print(user1)
banco.criar_conta(usuario=user1)
print(user1._status)

