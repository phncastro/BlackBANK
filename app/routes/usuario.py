from fastapi import APIRouter, Depends, HTTPException
from app.schemas.usuario import UsuarioCreate, UsuarioCreateResponse, UsuarioSolicitacaoResponse
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.services.usuario_service import UsuarioService


usuario_router = APIRouter(prefix='/usuarios')

@usuario_router.post('/criar-usuario/',
    response_model= UsuarioCreateResponse)
def criar_usuario(
    usuario: UsuarioCreate,
    db:Session=Depends(get_db)):

    db_usuario = Usuario(nome= usuario.nome, cpf= usuario.cpf, email= usuario.email)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)

    return {"mensagem": "Usuário criado com sucesso", "usuario_id": db_usuario.id} 

@usuario_router.post('/{id}/solicitar-conta/',
    response_model= UsuarioSolicitacaoResponse)
def solicitar_conta(
    id:int,
    db:Session=Depends(get_db)):

    db_usuario = db.query(Usuario).filter(Usuario.id == id).first()

    if db_usuario is None:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    
    UsuarioService.solicitar_criacao_de_conta(db_usuario)
    db.commit()

    return {"mensagem": "Conta solicitada com sucesso", "status": db_usuario.status}
