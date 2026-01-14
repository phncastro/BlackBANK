from models.usuario import Usuario
from core.exceptions import CriacaoDeContaNegadaError
from random import randint
from services.usuario_service import UsuarioService
from core.status_usuario import StatusUsuario
from models.conta import Conta

class BancoService:
    def criar_conta(self, usuario: Usuario):
        ''' 
        parâmetros: 

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

        UsuarioService._ativar_conta(usuario)
        return conta

    def _gerar_numero_da_conta():
        '''
        Gera o número da conta.
        '''
        return  str(randint(1, 9999)).zfill(4)
        

        


            

    


