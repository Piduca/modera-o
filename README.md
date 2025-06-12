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

Projeto criado para disciplina de Sistemas Distribuídos




