from pydantic import BaseModel
from core.status_usuario import StatusUsuario

class UsuarioCreate(BaseModel):
    nome : str
    cpf: str

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    cpf: str
    status: StatusUsuario