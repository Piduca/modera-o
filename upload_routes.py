from fastapi import APIRouter, UploadFile, File
import os
import uuid
import json
import pika
from db.db import SessionLocal, ConteudoModerado

router = APIRouter()

RABBITMQ_HOST = "localhost"
QUEUE_TEXTO = "moderacao.texto"
QUEUE_IMAGEM = "moderacao.imagem"
QUEUE_AUDIO = "moderacao.audio"

connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_TEXTO, durable=True)
channel.queue_declare(queue=QUEUE_IMAGEM, durable=True)
channel.queue_declare(queue=QUEUE_AUDIO, durable=True)

def publicar_na_fila(queue, payload):
    channel.basic_publish(
        exchange='',
        routing_key=queue,
        body=json.dumps(payload),
        properties=pika.BasicProperties(delivery_mode=2)
    )

def salvar_conteudo(id, tipo, caminho=None, conteudo=None, status="pendente"):
    db = SessionLocal()
    try:
        novo = ConteudoModerado(id=id, tipo=tipo, caminho=caminho, conteudo=conteudo, status=status)
        db.add(novo)
        db.commit()
    finally:
        db.close()

@router.post("/upload/texto")
def upload_texto(conteudo: str):
    id = str(uuid.uuid4())
    payload = {
        "id": id,
        "tipo": "texto",
        "conteudo": conteudo
    }
    salvar_conteudo(id=id, tipo="texto", conteudo=conteudo)
    publicar_na_fila(QUEUE_TEXTO, payload)
    return {"status": "Texto enviado para moderação", "id": id}

@router.post("/upload/imagem")
async def upload_imagem(file: UploadFile = File(...)):
    os.makedirs("temp", exist_ok=True)
    id = str(uuid.uuid4())
    caminho = f"temp/{id}_{file.filename}"
    with open(caminho, "wb") as buffer:
        buffer.write(await file.read())

    payload = {
        "id": id,
        "tipo": "imagem",
        "caminho": caminho
    }
    salvar_conteudo(id=id, tipo="imagem", caminho=caminho)
    publicar_na_fila(QUEUE_IMAGEM, payload)
    return {"status": "Imagem enviada para moderação", "id": id}

@router.post("/upload/audio")
async def upload_audio(file: UploadFile = File(...)):
    os.makedirs("temp", exist_ok=True)
    id = str(uuid.uuid4())
    caminho = f"temp/{id}_{file.filename}"
    with open(caminho, "wb") as buffer:
        buffer.write(await file.read())

    payload = {
        "id": id,
        "tipo": "audio",
        "caminho": caminho
    }
    salvar_conteudo(id=id, tipo="audio", caminho=caminho)
    publicar_na_fila(QUEUE_AUDIO, payload)
    return {"status": "Áudio enviado para moderação", "id": id}