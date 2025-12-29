from models.usuario import Usuario
from banco.banco import Banco

user1 = Usuario('Pablo', '10492456607')
user2 = Usuario('Joao', '01234567891')
user3 = Usuario('Claudio', '05242351758')

print(user1)
user1.solicitar_criacao_de_conta()
user2.solicitar_criacao_de_conta()
user3.solicitar_criacao_de_conta()
print(user1)
Banco.criar_conta(user1)
print(user1)
print(user2)
print(user3)

