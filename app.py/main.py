from models.usuario import Usuario
from models.banco import Banco
from core.exceptions import (
    TransicaoDeEstadoInvalidaError,
    CriacaoDeContaNegadaError
)

def teste_fluxo_completo():
    banco = Banco()
    usuario = Usuario("Pablo", "10492456607")
    usuario2 = Usuario('Nicolas', '10492457689')

    print("Status inicial:", usuario.status)

    try:
        usuario.solicitar_criacao_de_conta()
        usuario2.solicitar_criacao_de_conta()
        print("Após solicitação:", usuario.status)

        conta = banco.criar_conta(usuario)
        conta2 = banco.criar_conta(usuario2)
        print("Após criação:", usuario.status)

        conta.depositar(1000)
        conta.transferir(conta2, 250)
        print("Depósito OK")

        conta.sacar(500)
        print(conta2._saldo)

        print("Saque OK")
        print(conta._saldo)

    except (TransicaoDeEstadoInvalidaError, CriacaoDeContaNegadaError, ValueError) as erro:
        print("Erro:", erro)

if __name__ == "__main__":
    teste_fluxo_completo()
