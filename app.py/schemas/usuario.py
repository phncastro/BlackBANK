from pydantic import BaseModel
from core.status_usuario import StatusUsuario
from models.conta import Conta

class UsuarioCreate(BaseModel):
    nome : str
    cpf: str

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    cpf: str
    status: StatusUsuario
    conta: Conta