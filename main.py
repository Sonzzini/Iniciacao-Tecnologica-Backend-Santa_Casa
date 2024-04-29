from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Conexão com MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['meubanco']
collection = db['meucollection']

@app.route('/add', methods=['POST'])
def add_item():
    item = request.json
    collection.insert_one(item)
    return jsonify({'status': 'Item adicionado com sucesso!'}), 201


@app.route('/list', methods=['GET'])
def list_items():
    items = list(collection.find({}, {'_id': 0}))
    return jsonify(items), 200


@app.route('/')
def quick_test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)

