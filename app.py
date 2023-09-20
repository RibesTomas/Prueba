from flask import Flask, jsonify, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/ping')
def ping():
    return jsonify({'message':'pong'})

@app.route('/usuarios/<string:nombre>')
def usuario_by_name(nombre):
    return jsonify({'name': nombre})

@app.route('/usuarios/<int:id>')
def usuario_by_id(id):
    return jsonify({'id': id})


@app.route('/<path:nombre>')
def no_hacer(nombre):
    return escape(nombre)

@app.route('/recurso' , methods=['GET'])
def get_recursos():
    return jsonify({'data': 'lista de todos los items de este recursos'})

#post nuevo 'Recurso'
@app.route('/recurso' , methods=['POST'])
def POST_recursos():
    print(request.get_json())
    body = request.get_json()
    name = body['name']
    modelo = body['modelo']
    #insertar en la db
    return jsonify({'recurso': {
                    'name':name,
                    'modelo':modelo}})

#recurso por ID
@app.route('/recurso/<int:id>', methods = ['GET'])
def get_recurso_by_id(id):
    return jsonify({"recurso": {
        "name" : "name del id",
        "modelo": "modelo del id"
    }})











if __name__ == '__main__':
    app.run(debug=True, port=5000)