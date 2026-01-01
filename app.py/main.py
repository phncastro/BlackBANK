from models.usuario import Usuario
from models.banco import Banco
from core.exceptions import (
    TransicaoDeEstadoInvalidaError,
    CriacaoDeContaNegadaError
)

def teste_fluxo_completo():
    banco = Banco()
    usuario = Usuario("Pablo", "10492456607")

    print("Status inicial:", usuario.status)

    try:
        usuario.solicitar_criacao_de_conta()
        print("Após solicitação:", usuario.status)

        conta = banco.criar_conta(usuario)
        print("Após criação:", usuario.status)

        conta.depositar(1000)
        print("Depósito OK")

        conta.sacar(1200)
        print("Saque OK")

    except (TransicaoDeEstadoInvalidaError, CriacaoDeContaNegadaError, ValueError) as erro:
        print("Erro:", erro)

if __name__ == "__main__":
    teste_fluxo_completo()
