from contextlib import redirect_stderr

from flask import Flask, request, url_for
import json
import requests

app = Flask(__name__)


# Métodos despues de esta linea

@app.route("/")
def hello():
    data = {"api": "rest :"}
    return json.dumps(data)


@app.route("/auth/login", methods=['POST'])
def log_auth():
    values = requests.get_json()
    if values['usuario'] == 'admin' and values['clave'] == 'top_secret':
        respuesta = {'error': False, 'mensaje': 'Auser logged'}
        return json.dumps(respuesta)
    respuesta = {'error': True, 'mensaje': 'Fail Auth'}
    return json.dumps(values, respuesta)


@app.route("/prueba")
def prueba():
    datos = {"Aqui debería haber algo": "holi"}
    return json.dumps(datos)


@app.route("/app/api/post", methods=["GET"])
def api_post():
    data = []

    for i in range(10):
        # Generamos contenido
        data.append({
            "titulo": "titulo,",
            "detalles": "lorem Lorem Ipsum es simplemente texto de relleno de la industria de la impresión y la composición tipográfica.",
            "tagas": ["android", "nodejs", "javascript"]
        })

    return json.dumps(data)


@app.route("/app/api/post//", methods=["GET"])
def details_post(id):
    data = {
        "titulo": "titulo {} ".format(id),
        "detalles": "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
        "tags": ["android", "nodejs", "javascript"]
    }

    return json.dumps(data)


if __name__ == "__main__":
    app.run(debug=True, port=8888)
