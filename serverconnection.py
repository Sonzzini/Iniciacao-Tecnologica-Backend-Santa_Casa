from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def main():
    try:
        # Conecta ao MongoDB, substitua localhost:27017 pelo seu endereço de servidor se necessário
        client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)
        # Tenta buscar o nome do servidor, o que força uma conexão e poderia lançar um erro
        print(client.server_info())  # Esta linha força uma conexão e busca informações
        print("Conexão com o MongoDB foi bem-sucedida!")
    except ConnectionFailure as e:
        print("Falha ao conectar ao MongoDB:", e)

if __name__ == '__main__':
    main()
