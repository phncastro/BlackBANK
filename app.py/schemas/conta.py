from pydantic import BaseModel

class Conta(BaseModel):
    id: int
    numero: int
    usuario_id: int