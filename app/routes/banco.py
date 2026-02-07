from fastapi import APIRouter, Depends, HTTPException
from app.database.database import get_db
from sqlalchemy.orm import Session, joinedload
from app.models.usuario import Usuario
from app.services.banco_service import BancoService
from app.schemas.conta import Conta
from typing import List
from app.schemas import usuario

banco_router = APIRouter(prefix='/banco')

##################################################################################
@banco_router.post('/criar-conta/{id}/',
    response_model=Conta)
def criar_conta(
    id:int,
    db:Session=Depends(get_db)):

    db_usuario = db.query(Usuario).filter(Usuario.id == id).first()

    if db_usuario == None:
        raise HTTPException(status_code=404, detail='ID de usuário não encontrada')
    
    conta = BancoService.criar_conta(db_usuario)
    db.add(conta)
    db.commit()
    db.refresh(conta)

    return conta

##################################################################################
@banco_router.get('/usuarios/',
    response_model= List[usuario.UsuarioBase])
def ler_usuarios(
    db:Session=Depends(get_db)):

    usuarios = db.query(Usuario).options(joinedload(Usuario.conta)).all()

    return usuarios

##################################################################################
@banco_router.get('/{id}/',
    response_model= usuario.UsuarioBase)
def consultar_usuario(
    id:int,
    db:Session=Depends(get_db)):

    db_usuario = db.query(Usuario).filter(Usuario.id==id).first()

    if db_usuario is None:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    
    return db_usuario

        
    