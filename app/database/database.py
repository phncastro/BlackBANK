from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

# Carrega a pasta .env(oculta) que detém a URL do database
load_dotenv()

# Define a URL da database, que foi carregado no load_dotenv
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria o meio de acesso ao database
engine = create_engine(DATABASE_URL)

# Abre a sessão com o database usando a engine
SessionLocal = sessionmaker(bind=engine)

# Declara os tipos do nosso database, os modelos herdam dele 
Base = declarative_base()

# Abre a sessão com o database, pausa o acesso durante o uso, e finaliza a sessão ao encerrar
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()