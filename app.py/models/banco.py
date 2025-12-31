from models.conta import Conta
from models.usuario import Usuario
from core.status_usuario import StatusUsuario
from core.exceptions import CriacaoDeContaNegadaError
from random import randint


class Banco:
    '''
    Banco = Classe que representa a instituição financeira,
    que faz a intermediação entre Usuário e Conta.
    '''

    def criar_conta(self, usuario: Usuario):
        ''' 
        parâmetros: 

        - self: Instância da classe Banco 
        - usuario: Usuário que deseja criar a conta.

        return: Erro, se o usuário não puder ter a conta criada, ou se puder,
        cria a conta e gera o número para essa conta.
        '''

        if usuario.status == StatusUsuario.SEM_CONTA:
            raise CriacaoDeContaNegadaError(
                'Para criar a conta é necessário o Usuário solicitar primeiro.'
                )
        
        if usuario.status == StatusUsuario.CONTA_ATIVA:
            raise CriacaoDeContaNegadaError(
                'Usuário já possui conta ativa.'
                )
        
        numero_gerado = self._gerar_numero_da_conta()
        conta = Conta(usuario, numero_gerado)

        usuario._ativar_conta()
        return conta

    def _gerar_numero_da_conta(self):
        '''
        Gera o número da conta.
        '''
        return  str(randint(1, 9999)).zfill(4)
        

        


            

    


