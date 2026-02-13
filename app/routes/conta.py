from fastapi import APIRouter, Depends, HTTPException
from app.schemas.conta import ContaTransferencia, ContaTransferenciaResponse, ContaTransacaoResponse, ContaTransacao
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.models.conta import Conta
from app.services.conta_service import ContaService
from app.models.transacao import Transacao
from app.core.transacoes import TipoTransacao
from datetime import datetime

# Prefixo dos endpoints de conta
conta_router = APIRouter(prefix='/conta', tags=['usuario'])


# Realiza depósito em uma conta através do número dela
@conta_router.post(
    '/depositos/',
    description='Realiza o depósito do valor na conta informada',
    response_model=ContaTransacaoResponse
)
def depositar(
    conta_e_valor:ContaTransacao,
    db:Session=Depends(get_db)
):
    db_conta = db.query(Conta).filter(Conta.numero == conta_e_valor.num_conta).first()
    if db_conta == None:
        raise HTTPException(status_code=404, detail='Conta não encontrada')
    ContaService.depositar(db_conta, conta_e_valor.valor)

    db_transacao = Transacao(
        tipo=TipoTransacao.DEPOSITO,
        valor=conta_e_valor.valor,
        num_conta=db_conta.numero,
        data_hora=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    db.add(db_transacao)
    db.commit()

    return {
        'id_transacao': db_transacao.id,
        'num_conta': db_conta.numero,
        'valor': conta_e_valor.valor,
        'saldo': db_conta.saldo,
        'data_hora': db_transacao.data_hora
    }


# Realiza o saque em conta através do número da mesma
@conta_router.post(
    '/saques/',
    description='Realiza o saque do valor na conta informada',
    response_model=ContaTransacaoResponse
)
def sacar(
    conta_e_valor:ContaTransacao,
    db:Session=Depends(get_db)
):
    db_conta = db.query(Conta).filter(Conta.numero == conta_e_valor.num_conta).first()
    if db_conta == None:
        raise HTTPException(status_code=404, detail='Conta não encontrada')
    ContaService.sacar(db_conta, conta_e_valor.valor)

    db_transacao = Transacao(
        tipo=TipoTransacao.SAQUE,
        valor=conta_e_valor.valor,
        id_conta=db_conta.numero,
        data_hora=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    db.add(db_transacao)
    db.commit()

    return {
        'id_transacao': db_transacao.id,
        'num_conta': db_conta.numero,
        'valor': conta_e_valor.valor,
        'saldo': db_conta.saldo,
        'data_hora': db_transacao.data_hora
    }


# Realiza transferência entre duas contas, através do número da conta
@conta_router.post(
    '/transferencias/',
    description='Realiza a transferência de um valor, de uma conta para outra usando os números de conta',
    response_model=ContaTransferenciaResponse
)
def transferir(
    contas_e_valor: ContaTransferencia,
    db:Session=Depends(get_db)
):
    db_conta = db.query(Conta).filter(Conta.numero == contas_e_valor.num_conta).first()
    db_destinatario = db.query(Conta).filter(Conta.numero == contas_e_valor.num_conta_destino).first()
    ContaService.transferir(db_conta, db_destinatario, contas_e_valor.valor)
    
    db_transacao = Transacao(
        tipo=TipoTransacao.TRANSFERENCIA,
        valor=contas_e_valor.valor,
        num_conta=db_conta.numero,
        num_conta_destino=db_destinatario.numero,
        data_hora=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
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