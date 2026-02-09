from fastapi import APIRouter, Depends, HTTPException
from app.schemas.conta import ContaTransferencia, ContaTransferenciaResponse, ContaTransacaoResponse, ContaTransacao
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.models.conta import Conta
from app.services.conta_service import ContaService
from app.models.transacao import Transacao
from app.core.transacoes import TipoTransacao
from datetime import datetime

conta_router = APIRouter(prefix='/conta')

# Pega a data e hora atual
agora = datetime.now()

# Formata para ANO-MÊS-DIA HORA:MINUTO:SEGUNDO
# %D=Dia, %m=Mês, %Y=Ano, %H=Hora(24h), %M=Minuto, %S=Segundo
data_segundos = agora.strftime("%d-%m-%Y %H:%M:%S")

##################################################################################
@conta_router.post('/depositos/',
    response_model=ContaTransacaoResponse)
def deposito(
    id_e_valor:ContaTransacao,
    db:Session=Depends(get_db)):

    db_conta = db.query(Conta).filter(Conta.id == id_e_valor.id).first()

    if db_conta == None:
        raise HTTPException(status_code=404, detail='Conta não encontrada')
    
    ContaService.depositar(db_conta, id_e_valor.valor)

    db_transacao = Transacao(
        tipo=TipoTransacao.DEPOSITO,
        valor=id_e_valor.valor,
        id_conta=db_conta.id,
        data_hora=data_segundos)
    
    db.add(db_transacao)
    db.commit()

    return {
        'id_transacao': db_transacao.id,
        'num_conta': db_conta.numero,
        'valor': id_e_valor.valor,
        'saldo': db_conta.saldo,
        'data_hora': db_transacao.data_hora
    }

##################################################################################
@conta_router.post('/saques/',
    response_model=ContaTransacaoResponse)
def saque(
    id_e_valor:ContaTransacao,
    db:Session=Depends(get_db)):

    db_conta = db.query(Conta).filter(Conta.id == id_e_valor.id).first()

    if db_conta == None:
        raise HTTPException(status_code=404, detail='Conta não encontrada')
    
    ContaService.sacar(db_conta, id_e_valor.valor)

    db_transacao = Transacao(
        tipo=TipoTransacao.SAQUE,
        valor=id_e_valor.valor,
        id_conta=db_conta.id,
        data_hora=data_segundos)
    
    db.add(db_transacao)
    db.commit()

    return {
        'id_transacao': db_transacao.id,
        'num_conta': db_conta.numero,
        'valor': id_e_valor.valor,
        'saldo': db_conta.saldo,
        'data_hora': db_transacao.data_hora
    }

##################################################################################
@conta_router.post('/transferencias/',
    response_model=ContaTransferenciaResponse)
def transferencia(
    contas_e_valor: ContaTransferencia,
    db:Session=Depends(get_db)):

    db_conta = db.query(Conta).filter(Conta.numero == contas_e_valor.num_conta).first()
    db_destinatario = db.query(Conta).filter(Conta.numero == contas_e_valor.num_conta_destino).first()

    ContaService.transferir(db_conta, db_destinatario, contas_e_valor.valor)
    
    db_transacao = Transacao(
        tipo=TipoTransacao.TRANSFERENCIA,
        valor=contas_e_valor.valor,
        id_conta=db_conta.id,
        id_conta_destino=db_destinatario.id,
        data_hora=data_segundos)
    
    db.add(db_transacao)
    db.commit()
    
    return {
        'id_transacao': db_transacao.id,
        'num_conta': db_conta.numero,
        'num_conta_destino': db_destinatario.numero,
        'valor': contas_e_valor.valor,
        'saldo': db_conta.saldo,
        'data_hora': db_transacao.data_hora
    }