from pydantic import BaseModel, ConfigDict, field_validator
from typing import Optional
from app.schemas.conta import Conta
from app.core.validators.cpf import validar_cpf
from app.core.validators.email import validar_email
from app.core.validators.nome import validar_nome
from app.core.status_usuario import StatusUsuario

class UsuarioBase(BaseModel):
    id: int
    nome: str
    cpf: str
    email: str 
    status: StatusUsuario
    conta: Optional[Conta] = None
    model_config = ConfigDict(from_attributes=True)

class UsuarioCreate(BaseModel):
    nome : str
    cpf: str
    email: str
    model_config = ConfigDict(from_attributes=True)

    @field_validator('nome')
    @classmethod
    def nome_valido(cls, nome):
        return validar_nome(nome)

    @field_validator('cpf')
    @classmethod
    def cpf_valido(cls, cpf):
        return validar_cpf(cpf)
    
    @field_validator('email')
    @classmethod
    def email_valido(cls, email):
        return validar_email(email)

class UsuarioSolicitacaoResponse(BaseModel):
    id: int
    status: StatusUsuario
    model_config = ConfigDict(from_attributes=True)