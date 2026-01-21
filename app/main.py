from fastapi import FastAPI
from app.routes.usuario import usuario_router
from app.routes.conta import conta_router
from app.routes.banco import banco_router
from app.database.database import Base
from app.database.database import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuario_router)
app.include_router(conta_router)
app.include_router(banco_router)