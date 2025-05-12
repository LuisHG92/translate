from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    source = data.get("source", "en")
    target = data.get("target", "es")

    res = requests.post("https://libretranslate.com/translate", data={
        "q": text,
        "source": source,
        "target": target,
        "format": "text"
    })

    return jsonify(res.json())

@app.route("/")
def home():
    return "Servidor activo. Usa POST /translate para traducir texto."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)