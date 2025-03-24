# Usando imagem oficial do Python
FROM python:3.12

# Criando diretório de trabalho dentro do container
WORKDIR /app

# Definir PATH do Python
ENV PYTHONPATH=/app

# Copiar os arquivos de dependências primeiro
COPY requirements.txt /app/requirements.txt

# Instalar as dependências antes do código
RUN pip install --no-cache-dir -r /app/requirements.txt

# Agora copie o código-fonte da aplicação corretamente
COPY app /app

# Expõe a porta do Flask
EXPOSE 5000

# Comando para rodar o Flask com Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "wsgi:app"]

