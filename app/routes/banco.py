from fastapi import APIRouter, Depends, HTTPException
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.services.banco_service import BancoService
from app.schemas.conta import Conta

banco_router = APIRouter(prefix='/banco')

@banco_router.post('/criar-conta/{id}', response_model=Conta)
def criar_conta(id:int, db:Session=Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if db_usuario == None:
        raise HTTPException(status_code=404, detail='ID de usuário não encontrada')
    conta = BancoService.criar_conta(db_usuario)
    return conta
    