from pydantic import BaseModel, ConfigDict
from datetime import datetime

class Conta(BaseModel):
    id: int
    numero: str
    saldo: float
    usuario_id: int
    model_config = ConfigDict(from_attributes=True)

class ContaCreate(BaseModel):
    numero: str
    usuario_id: int
    model_config = ConfigDict(from_attributes=True)

class ContaTransacao(BaseModel):
    id: int
    valor: float

class ContaTransacaoResponse(BaseModel):
    id_transacao: int
    num_conta: str
    valor: int
    saldo: float
    data_hora = datetime

class ContaTransferencia(BaseModel):
    num_conta: str
    num_conta_destino: str
    valor: float

class ContaTransferenciaResponse(BaseModel):
    id_transacao: int
    num_conta: str
    num_conta_destino: str
    valor: int
    saldo: float
    data_hora = datetime