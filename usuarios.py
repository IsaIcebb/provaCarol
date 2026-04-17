from flask import Flask, jsonify
import os

app = Flask(__name__)

usuarios = [
    {"id": 1, "usuarios": "Miriam"},
    {"id": 2, "usuarios": "Sophia"},
    {"id": 3, "usuarios": "Miguel "},
    {"id": 4, "usuarios": "Isadora"},
    {"id": 5, "usuarios": "Ana Paula"},
    {"id": 6, "usuarios": "Cassia"},
    {"id": 7, "usuarios": "Roberto"},
    {"id": 8, "usuarios": "Juliana"},
    {"id": 9, "usuarios": "Júlio"},
    {"id": 10, "usuarios": "Pedro"},
    {"id": 11, "usuarios": "Renata"},
    {"id": 12, "usuarios": "Maria"},
    {"id": 13, "usuarios": "Cacilda"},
    {"id": 14, "usuarios": "Isobelle"},
    {"id": 15, "usuarios": "Lenora"},
    
]

@app.route("/usuarios", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de usuarios - Acesse /usuarios"})

@app.route("/", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == "__main__":
    port = int(os.environ.get("PORT" , 5000))
    app.run(host="0.0.0.0", port=port)
