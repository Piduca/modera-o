import pika
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api import ConteudoModerado, DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

RABBITMQ_HOST = 'localhost'
QUEUE_TEXTO = 'moderacao.texto'

def processar_texto(texto):
    if "proibido" in texto.lower():
        return "Rejeitado"
    return "Aprovado"

def atualizar_status(id, status):
    db = SessionLocal()
    try:
        conteudo = db.query(ConteudoModerado).filter(ConteudoModerado.id == id).first()
        if conteudo:
            conteudo.status = status
            db.commit()
    finally:
        db.close()

def callback(ch, method, properties, body):
    dados = json.loads(body)
    print(f"[WORKER TEXTO] Recebido ID {dados['id']}")
    
    resultado = processar_texto(dados["conteudo"])
    print(f"[RESULTADO] {dados['id']} → {resultado}")

    atualizar_status(dados["id"], resultado)
    ch.basic_ack(delivery_tag=method.delivery_tag)

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    print("[WORKER TEXTO] Conexão com RabbitMQ estabelecida.")
    
    channel.queue_declare(queue=QUEUE_TEXTO, durable=True)
    print("[WORKER TEXTO] Fila declarada com sucesso.")

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_TEXTO, on_message_callback=callback)

    print("[WORKER TEXTO] Aguardando mensagens...")
    channel.start_consuming()
except pika.exceptions.AMQPConnectionError as e:
    print(f"Erro ao conectar ao RabbitMQ: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
