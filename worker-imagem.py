import pika
import json
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.db import ConteudoModerado, DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

RABBITMQ_HOST = 'localhost'
QUEUE_IMAGEM = 'moderacao.imagem'

def moderar_imagem(path):
    time.sleep(2)
    if "inapropriada" in path:
        return "Rejeitado"
    return "Aprovado"

def atualizar_status(id, status):
    db = SessionLocal()
    item = db.query(ConteudoModerado).filter(ConteudoModerado.id == id).first()
    if item:
        item.status = status
        db.commit()
    db.close()

def callback(ch, method, properties, body):
    dados = json.loads(body)
    resultado = moderar_imagem(dados["caminho"])
    print(f"[MOD IMAGEM] ID {dados['id']} → {resultado}")
    atualizar_status(dados["id"], resultado)
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_IMAGEM, durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=QUEUE_IMAGEM, on_message_callback=callback)

print("[WORKER IMAGEM] Aguardando mensagens...")
channel.start_consuming()

