from table import new_table
from player import Player, juant
from app import app
from flask import jsonify


@app.route("/")
def index():
    return 'Hello World'

@app.route('/get-drop')
def recieve_drop():
    try:
        drop = new_table.get_drop(juant)
        return jsonify({'Inventory': drop}), 200
    except Exception as e:
        return jsonify({'error', str(e)}), 500


@app.route('/get-drop/drop-current', methods=['GET', 'DELETE'])
def drop_item():
    remove_previous = juant.drop_item()
    return jsonify(remove_previous), 200

@app.route('/clear-inventory', methods=['GET', 'POST'])
def clear_inv():
    clear_inv = juant.clear_inventory()
    return jsonify(clear_inv)