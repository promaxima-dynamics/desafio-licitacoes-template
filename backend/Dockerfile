# Use uma imagem Python oficial como base
FROM python:3.10-slim

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho no container
WORKDIR /app

# Instala dependências do sistema se necessário (ex: build-essential para algumas libs)
RUN apt-get update && apt-get install -y --no-install-recommends curl netcat-traditional procps

# Copia o arquivo de dependências primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do backend para o diretório de trabalho
COPY . .

# Expõe a porta que o Django runserver usa
EXPOSE 8000

# Comando padrão para rodar a aplicação (pode ser sobrescrito no docker-compose)
# Use gunicorn ou uwsgi para produção
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 
