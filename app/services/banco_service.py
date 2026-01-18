from app.models.usuario import Usuario
from app.core.exceptions import CriacaoDeContaNegadaError
from random import randint
from app.services.usuario_service import UsuarioService
from app.core.status_usuario import StatusUsuario
from app.models.conta import Conta

class BancoService:
    ''' Classe que guarda e realiza os métodos do banco '''

    @staticmethod
    def _gerar_numero_da_conta():
        '''
        Gera o número da conta.
        '''
        numero = str(randint(1, 9999)).zfill(4)
        return  int(numero)


    @staticmethod
    def criar_conta(usuario: Usuario):
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
        
        numero_gerado = BancoService._gerar_numero_da_conta()
        conta = Conta(numero=numero_gerado, usuario_id= usuario.id)

        UsuarioService._ativar_conta(usuario)
        return conta

        


            

    


