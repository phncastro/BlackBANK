from fastapi import FastAPI, APIRouter
from schemas.usuario import UsuarioCreate, UsuarioResponse
from models.usuario import Usuario

usuario = APIRouter()

@usuario.post('/usuarios')
def criar_usuario(usuario: UsuarioCreate) -> UsuarioResponse:
    return [
        usuario(nome=usuario.nome, cpf=usuario.cpf)  
        ]
    

@usuario.post('/usuarios/{id}/solicitar-conta')
def a():
    ...     