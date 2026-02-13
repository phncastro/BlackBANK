from fastapi import APIRouter, Depends, HTTPException, status
from app.database.database import get_db
from sqlalchemy.orm import Session, joinedload
from app.models.usuario import Usuario
from app.services.banco_service import BancoService
from app.schemas.conta import Conta
from typing import List
from app.schemas import usuario
from datetime import datetime
from app.models.estado import Estado
from app.core.status_usuario import StatusUsuario

# Prefixo dos endpoints do banco
banco_router = APIRouter(prefix='/banco', tags=['banco'])


# Cria conta para o Usuário
@banco_router.post(
    '/criar-conta/{user_id}/',
    description='Cria uma conta para o usuário com o user_id fornecido, se o mesmo tiver solicitado',
    status_code=status.HTTP_201_CREATED,
    response_model=Conta
)
def criar_conta(
    user_id:int,
    db:Session=Depends(get_db)
):
    db_usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if db_usuario == None:
        raise HTTPException(status_code=404, detail='ID de usuário não encontrada')
    conta = BancoService.criar_conta(db_usuario)

    db.add(Estado(
        estado_anterior=StatusUsuario.SOLICITACAO_PENDENTE,
        estado_atual=StatusUsuario.CONTA_ATIVA,
        data_hora=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    db.add(conta)
    db.commit()
    db.refresh(conta)

    return conta


# Entrega todos os usuários cadastrados
@banco_router.get(
    '/usuarios/',
    description='Retorna todos os usuários cadastrados',
    response_model= List[usuario.UsuarioBase]
)
def ler_usuarios(
    db:Session=Depends(get_db)
):
    usuarios = db.query(Usuario).options(joinedload(Usuario.conta)).all()

    return usuarios


# Consulta um usuário através do user_id
@banco_router.get(
    '/{user_id}/',
    description='Retorna o usuário com o user_id fornecido',
    response_model= usuario.UsuarioBase
)
def consultar_usuario(
    user_id:int,
    db:Session=Depends(get_db)
):
    db_usuario = db.query(Usuario).filter(Usuario.id==user_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    
    return db_usuario