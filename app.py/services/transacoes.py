from models.conta import contas

class Transacoes:

    def transferir(self, cpf, valor):
        transferiu = False
        while not transferiu:
            try:
                valor = float(valor)
            except ValueError:
                print('Digite apenas números.')
            for conta in contas:
                if conta._cpf == cpf:
                    if self._saldo < 0:
                        print('Você nao possui saldo para essa transferência.')
                    elif self._saldo > 15000 and valor > 15000:
                        print('Para transferir este valor, entre em contato com o banco.')
                    elif valor > self._saldo:
                        print('Você nao possui saldo para realizar esta transferência.')
                    else:
                        self._saldo -= valor
                        conta._saldo += valor
                        transferiu = True
                        break
