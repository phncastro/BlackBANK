from fastapi import APIRouter, Depends, HTTPException
from app.schemas.conta import ContaDepositoResponse, ContaDeposito, ContaSaqueResponse, ContaSaque, ContaTransferenciaResponse, ContaTransferencia
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.models.conta import Conta
from app.services.conta_service import ContaService

conta_router = APIRouter(prefix='/conta')

@conta_router.post('/depositos ', response_model=ContaDepositoResponse)
def deposito(id_e_valor:ContaDeposito, db:Session=Depends(get_db)):
    db_conta = db.query(Conta).filter(Conta.id == id_e_valor.id).first()
    if db_conta == None:
        raise HTTPException(status_code=404, detail='Conta não encontrada')
    ContaService.depositar(db_conta, id_e_valor.valor)
    db.commit()
    return db_conta

@conta_router.post('/saques', response_model=ContaSaqueResponse)
def saque(id_e_valor:ContaSaque, db:Session=Depends(get_db)):
    db_conta = db.query(Conta).filter(Conta.id == id_e_valor.id).first()
    if db_conta == None:
        raise HTTPException(status_code=404, detail='Conta não encontrada')
    ContaService.sacar(db_conta, id_e_valor.valor)
    db.commit()
    return db_conta

@conta_router.post('/transferencias', response_model=ContaTransferenciaResponse)
def transferencia(id_iddestinatario_valor: ContaTransferencia, db:Session=Depends(get_db)):
    db_conta = db.query(Conta).filter(Conta.id == id_iddestinatario_valor.id).first()
    db_destinatario = db.query(Conta).filter(Conta.id == id_iddestinatario_valor.destinatario_id).first()
    ContaService.transferir(db_conta, db_destinatario, id_iddestinatario_valor.valor)
    db.commit()
    return db_conta