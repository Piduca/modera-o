from fastapi import APIRouter, HTTPException
from db.db import SessionLocal, ConteudoModerado

router = APIRouter()

@router.get("/status/{id}")
def verificar_status(id: str):
    db = SessionLocal()
    try:
        conteudo = db.query(ConteudoModerado).filter(ConteudoModerado.id == id).first()
        if not conteudo:
            raise HTTPException(status_code=404, detail="Conteúdo não encontrado")
        return {
            "id": conteudo.id,
            "tipo": conteudo.tipo,
            "status": conteudo.status,
            "caminho": conteudo.caminho,
            "conteudo": conteudo.conteudo
        }
    finally:
        db.close()

