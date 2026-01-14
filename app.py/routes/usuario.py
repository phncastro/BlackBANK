from fastapi import APIRouter, Depends, HTTPException
from schemas.usuario import UsuarioCreate, UsuarioResponse
from database.database import get_db
from sqlalchemy.orm import Session
from models.usuario import Usuario
from services.usuario_service import UsuarioService


usuario_router = APIRouter(prefix='/usuarios')

@usuario_router.post('/', response_model= UsuarioResponse)
def criar_usuario(usuario: UsuarioCreate, db:Session=Depends(get_db)):
    db_usuario = Usuario(nome= usuario.nome, cpf= usuario.cpf)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
    
@usuario_router.get('/{id}', response_model= UsuarioResponse)
def consultar_usuario(id:int, db:Session=Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id==id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return db_usuario

@usuario_router.post('/{id}/solicitar-conta', response_model= UsuarioResponse)
def solicitar_conta(id:int, db:Session=Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id == id).first()
    solicitacao = UsuarioService.solicitar_criacao_de_conta(db_usuario)
    return solicitacao
