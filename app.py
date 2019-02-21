from flask import Flask, abort,jsonify, request
import json
import requests 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return "Hello World !"

@app.route('/pokemons', methods=['GET'])
def get_pokemons():
    pokemon_id = request.args.get('pokemon', type=str)
    print(pokemon_id)
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemon_id + "/").content
    json_response = json.loads(response)
    return jsonify(json_response)

@app.route('/popo', methods=['GET'])
def get_all_pokemons():
    response = requests.get('https://pokeapi.co/api/v2/pokemon/').content
    json_response = json.loads(response)
    print(json_response)
    # return_all = {
    #     "results": json_response['results']
    # }
    return jsonify(json_response)

