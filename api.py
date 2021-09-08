from flask import Flask
from flask_restful import Resource, Api

#Crear instancia de flask
#le damos instancia de flask a Api
app = Flask(__name__)
api = Api(app)

#La clase hello hereda de Resource
class Hello(Resource):
    def get(self, name):
        return {"hello": name}

#Recurso a la API y asociación con ruta
api.add_resource(Hello, '/hello/<name>')

#correr aplicación
if __name__ == '__main__':
    app.run(debug=True)

