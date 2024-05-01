from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Conexão com MongoDB
client = MongoClient('mongodb://mongo:27017/')
db = client['meubanco']
collection = db['meucollection']
users_collection = db['userscollection']
clients_collection = db['clientscollection']


@app.route('/add', methods=['POST'])
def add_item():
    app.logger.debug('Received request: %s', request.data)
    try:
        item = request.json
        app.logger.debug('Parsed JSON: %s', item)
        collection.insert_one(item)
        return jsonify({'status': 'Item adicionado com sucesso!'}), 201
    except Exception as e:
        app.logger.error('An error occurred: %s', e)
        raise


@app.route('/list', methods=['GET'])
def list_items():
    items = list(collection.find({}, {'_id': 0}))
    return jsonify(items), 200


@app.route('/')
def quick_test():
    return render_template('test.html')


@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    data = request.form
    email = data.get('email')
    senha = data.get('senha')
    if email and senha:
        user_data = {'email': email, 'senha': senha}
        users_collection.insert_one(user_data)
        return jsonify({'message': 'Usuário cadastrado com sucesso!'})
    else:
        return jsonify({'error': 'É necessário fornecer email e senha!'}), 400


@app.route('/login', methods=['POST'])
def login():
    data = request.form
    email = data.get('email')
    senha = data.get('senha')
    user = users_collection.find_one({'email': email, 'senha': senha})
    if user:
        return jsonify({'message': 'Login bem-sucedido!'})
    else:
        return jsonify({'error': 'Credenciais inválidas'}), 401


@app.route('/cadastro_cliente', methods=['POST'])
def cadastrar_cliente():
    data = request.form
    identificador = data.get('identificador')
    nome = data.get('nome')
    data_nascimento = datetime.strptime(data.get('data_nascimento'), '%Y-%m-%d')
    sexo = data.get('sexo')
    observacoes = data.get('observacoes')
    imagem = request.files['imagem']
    data_cadastro = datetime.strptime(data.get('data_cadastro'), '%Y-%m-%d %H:%M:%S')
    if identificador and nome and data_nascimento and sexo and observacoes and imagem and data_cadastro:
        client_data = {
            'identificador': identificador,
            'nome': nome,
            'data_nascimento': data_nascimento,
            'sexo': sexo,
            'observacoes': observacoes,
            'imagem': imagem.read(),
            'data_cadastro': data_cadastro
        }
        clients_collection.insert_one(client_data)
        return jsonify({'message': 'Cliente cadastrado com sucesso!'})
    else:
        return jsonify({'error': 'Todos os campos são obrigatórios!'}), 400


@app.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = []
    for client in clients_collection.find():
        client['_id'] = str(client['_id'])
        clientes.append(client)
    return jsonify(clientes)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

