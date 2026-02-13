from pydantic import BaseModel, ConfigDict
from datetime import datetime

# Válida todos os campos de Conta
class Conta(BaseModel):
    id: int
    numero: str
    saldo: float
    usuario_id: int
    criada_em: datetime
    model_config = ConfigDict(from_attributes=True)

# Válida criação de conta
class ContaCreate(BaseModel):
    numero: str
    usuario_id: int
    model_config = ConfigDict(from_attributes=True)

# Válida dados de transação(Depósito/Saque)
class ContaTransacao(BaseModel):
    num_conta: str
    valor: float

# Válida response body de transações(Depósito/Saque)
class ContaTransacaoResponse(BaseModel):
    id_transacao: int
    num_conta: str
    valor: int
    saldo: float
    data_hora: datetime

# Válida dados para transferência
class ContaTransferencia(BaseModel):
    num_conta: str
    num_conta_destino: str
    valor: float

# Válida response body de transferência
class ContaTransferenciaResponse(BaseModel):
    id_transacao: int
    num_conta: str
    num_conta_destino: str
    valor: int
    saldo: float
    data_hora: datetime