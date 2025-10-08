from flask import Flask, render_template, jsonify
import os
import json

app = Flask(__name__)

ARCHIVO_JSON = "characters.json"

diccionario = {}


@app.route("/")
def index():
    return render_template("index.html")

def read_json(JSON_FILE: str):
    if not os.path.exists(JSON_FILE):
        return {"characters": []}
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Asegurar que la estructura sea correcta
            if 'characters' not in data:
                return {"characters": []}
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        return {"characters": []}

def write_json(data, JSON_FILE:str):
    # Asegurar que la estructura sea correcta
    if 'characters' not in data:
        data = {"characters": data}
    
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


@app.route('/api/characters', methods=['GET'])
def get_characters():
    try:
        data = read_json(ARCHIVO_JSON)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/characters/<int:character_id>', methods=['GET'])
def get_character_id(character_id: int):
    try:
        data = read_json(ARCHIVO_JSON)
        character = next((c for c in data['characters'] if c['id'] == character_id), None)
        if character:
            return jsonify(character)
        return jsonify({"error": "Character not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)