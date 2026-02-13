from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.usuario import UsuarioCreate, UsuarioBase, UsuarioSolicitacaoResponse
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.services.usuario_service import UsuarioService
from datetime import datetime
from app.models.estado import Estado
from app.core.status_usuario import StatusUsuario

# Prefixo dos endpoints de usuario
usuario_router = APIRouter(prefix='/usuario', tags=['usuario'])


# Cria um novo usuário
@usuario_router.post(
    '/criar-usuario/',
    description='Cria um novo usuário',
    status_code=status.HTTP_201_CREATED,
    response_model=UsuarioBase
)
def criar_usuario(
    usuario: UsuarioCreate,
    db:Session=Depends(get_db)
):
    db_usuario = Usuario(
        nome=usuario.nome,
        cpf=usuario.cpf,
        email=usuario.email,
        criado_em=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)

    return db_usuario


# Usuário solicita a criação da conta ao Banco
@usuario_router.post(
    '/{user_id}/solicitar-conta/',
    description='Solicita a criação da conta do usuário para o banco',
    status_code=status.HTTP_201_CREATED,
    response_model= UsuarioSolicitacaoResponse
)
def solicitar_conta(
    user_id:int,
    db:Session=Depends(get_db)
):
    db_usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    UsuarioService.solicitar_criacao_de_conta(db_usuario)

    db.add(Estado(
        estado_anterior=StatusUsuario.SEM_CONTA,
        estado_atual=StatusUsuario.SOLICITACAO_PENDENTE,
        data_hora=datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
    db.commit()

    return db_usuario
