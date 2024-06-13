# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copie o conteúdo do diretório atual para o contêiner
COPY . .

# Comando para iniciar o Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]