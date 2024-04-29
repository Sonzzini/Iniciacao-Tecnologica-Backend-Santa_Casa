# Usar uma imagem base oficial do Python
FROM python:3.8-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo de dependências e instalar as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos da aplicação
COPY . .

# Expor a porta que o Flask usará
EXPOSE 5000

# Comando para executar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
