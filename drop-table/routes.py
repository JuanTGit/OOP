from table import new_table
from player import Player, juant
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return 'Hello World'

@app.route('/get-drop', methods=['GET', 'POST'])
def recieve_drop():
    drop = new_table.get_drop(juant)
    return jsonify({'Inventory': drop})