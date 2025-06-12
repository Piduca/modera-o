# Sistema Distribuído de Moderação de Conteúdo (Texto, Imagem, Áudio)

Este projeto é uma API distribuída que realiza **moderação automática de conteúdo** (texto, imagem, áudio) utilizando a arquitetura **Publish/Subscribe** com **RabbitMQ**, **FastAPI** e **PostgreSQL**.

---

## Tecnologias Usadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [RabbitMQ](https://www.rabbitmq.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Pika (RabbitMQ client)](https://pika.readthedocs.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Uvicorn](https://www.uvicorn.org/)

---

---

## Passos a seguir para a instalação e configuração

### 1. Clone o projeto

```bash
git clone https://github.com/piduca/moderacao.git
cd seu-repositorio/mensage

### 2. Crie e ativa o ambiente virtual

python -m venv venv
.\venv\Scripts\activate       # Windows
# source venv/bin/activate   # Linux/macOS

### 3. Instale depedências
pip install -r requirements.txt

### 4. Inicie o RabbitMQ (via Docker)
bash
Copiar
Editar
docker run -d --hostname my-rabbit --name rabbitmq `
  -p 5672:5672 -p 15672:15672 rabbitmq:3-management
Acesse o painel: http://localhost:15672
Login: guest | Senha: guest

🗄️ 5. Configure o PostgreSQL
Use o banco de dados moderacao da pasta mensage

Certifique-se de que seu DATABASE_URL está correto em db.py, por exemplo:

python
Copiar
Editar
DATABASE_URL = "postgresql://utilizador:senha@localhost:5432/moderacao"
🚀 Como Rodar o Projeto
1. Inicie a API FastAPI:
bash
Copiar
Editar
uvicorn api:app --reload
Acesse: http://127.0.0.1:8000/docs

2. Rode os workers em terminais separados:
bash
Copiar
Editar
python worker-texto.py
python worker-imagem.py
python worker-audio.py
🧪 Como Usar
▶️ Envie conteúdos para moderação:
POST /upload/texto – envia um campo conteudo

POST /upload/imagem – envia um arquivo .jpg, .png, etc.

POST /upload/audio – envia um arquivo .mp3, .wav, etc.

🔍 Verifique o status do conteúdo:
GET /status/{id} – retorna status: pendente, Aprovado, Rejeitado

## Passos a seguir para a comunicação entre 2 computadores
🔹 1. No PC que executa a API e RabbitMQ (servidor)
1.1 Descubra o IP local:

No terminal, execute:
ipconfig

Anote algo como:
IPv4 Address. . . . . . : 192.168.0.10
Esse é o endereço que os outros computadores usarão para acessar a API.

1.2 Rode a API com acesso liberado na rede:
uvicorn api:app --host 0.0.0.0 --port 8000 --reload

🔹 2. No PC cliente ou worker
2.1 Acesse a API remotamente via navegador ou terminal:
http://192.168.0.10:8000/docs
Substitua 192.168.0.10 pelo IP real do PC servidor.

2.2 Atualize os workers para conectar ao RabbitMQ remoto:

Exemplo para worker-texto.py, worker-audio.py, worker-imagem.py:
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.10'))
🔐 3. Ajustes de rede e firewall
Se o acesso falhar:
Certifique-se de que os dois PCs estão na mesma rede Wi-Fi ou LAN

Adicione exceções no Firewall do Windows para:
Python
Uvicorn (porta 8000)
RabbitMQ (portas 5672 e 15672)

Acesse o navegador no PC 2 e tente:
http://192.168.0.10:8000/docs

Projeto criado para disciplina de Sistemas Distribuídos




