# proxy_matriz.py
from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Permite que tu HTML haga fetch desde cualquier origen

# URL de la agencia Matriz
URL_MATRIZ = "https://jq-motors-inventarios-matriz.onrender.com/inventario"

@app.route("/proxy_matriz")
def proxy_matriz():
    try:
        resp = requests.get(URL_MATRIZ, timeout=5)
        resp.raise_for_status()
        datos = resp.json()
        # Agregar nombre de la agencia a cada item
        for item in datos:
            item["agencia"] = "Matriz"
        return jsonify(datos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5002)  # Puedes usar el mismo puerto que antes
