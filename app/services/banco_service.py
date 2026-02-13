from app.models.usuario import Usuario
from app.core.exceptions import CriacaoDeContaNegadaError
from random import randint
from app.services.usuario_service import UsuarioService
from app.core.status_usuario import StatusUsuario
from app.models.conta import Conta
from datetime import datetime

class BancoService:
    '''
    Realiza todos os métodos do Banco
    '''

    @staticmethod
    def _gerar_numero_da_conta():
        '''
        Gera o número da conta.
        '''
        numero = str(randint(1, 9999)).zfill(4)
        return  numero


    @staticmethod
    def criar_conta(usuario:Usuario):
        ''' 
        Verifica se o usuário pode ter a conta criada e cria se possível
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
        conta = Conta(
            numero=numero_gerado,
            usuario_id=usuario.id,
            criada_em=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        UsuarioService._ativar_conta(usuario)
        return conta

        


            

    


