from models.conta import Conta
from models.usuario import Usuario
from core.status_usuario import StatusUsuario
from core.exceptions import CriacaoDeContaNegadaError
from random import randint


class Banco:

    def criar_conta(self, usuario: Usuario):

        if usuario._status == StatusUsuario.SEM_CONTA:
            raise CriacaoDeContaNegadaError(
                'Para criar a conta é necessário o Usuário solicitar primeiro.'
                )
        
        if usuario._status == StatusUsuario.CONTA_ATIVA:
            raise CriacaoDeContaNegadaError(
                'Usuário já possui conta ativa.'
                )
        
        numero_gerado = self._gerar_numero_da_conta()
        conta = Conta(usuario, numero_gerado)

        usuario._ativar_conta()

    def _gerar_numero_da_conta(self):
        return  str(randint(1, 9999)).zfill(4)
        

        


            

    


