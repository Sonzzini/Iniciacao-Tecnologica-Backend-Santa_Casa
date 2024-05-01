from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Conexão com MongoDB
client = MongoClient('mongodb://mongo:27017/')
db = client['meubanco']
collection = db['meucollection']

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

