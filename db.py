from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:Princesa@localhost:5432/moderacao"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class ConteudoModerado(Base):
    __tablename__ = "conteudos"
    id = Column(String, primary_key=True, index=True)
    tipo = Column(String, index=True)
    caminho = Column(Text, nullable=True)
    conteudo = Column(Text, nullable=True)
    status = Column(String, default="pendente")

Base.metadata.create_all(bind=engine)
