from pydantic import BaseModel, ConfigDict

class Conta(BaseModel):
    id: int
    numero: int
    saldo: float
    model_config = ConfigDict(from_attributes=True)

class ContaCreate(BaseModel):
    numero: int
    usuario_id: int
    model_config = ConfigDict(from_attributes=True)

class ContaResponse(BaseModel):
    id: int
    numero: int
    usuario_id: int
    saldo: float
    model_config = ConfigDict(from_attributes=True)

class ContaDeposito(BaseModel):
    id: int
    valor: int


class ContaSaque(BaseModel):
    id: int
    valor: int


class ContaDepositoResponse(BaseModel):
    saldo: int
    model_config = ConfigDict(from_attributes=True)

class ContaSaqueResponse(BaseModel):
    saldo: int
    model_config = ConfigDict(from_attributes=True)

class ContaTransferenciaResponse(BaseModel):
    saldo: int
    model_config = ConfigDict(from_attributes=True)

class ContaTransferencia(BaseModel):
    id: int
    destinatario_id: int
    valor: int