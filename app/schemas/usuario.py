from pydantic import BaseModel, ConfigDict
from app.schemas.conta import Conta

class Usuario(BaseModel):
    id: int
    nome: str
    cpf: str
    status: int
    conta: Conta
    model_config = ConfigDict(from_attributes=True)

class UsuarioCreate(BaseModel):
    nome : str
    cpf: str
    model_config = ConfigDict(from_attributes=True)

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    cpf: str
    status: int
    model_config = ConfigDict(from_attributes=True)

class UsuarioSolicitacaoResponse(BaseModel):
    id: int
    status: int
    model_config = ConfigDict(from_attributes=True)