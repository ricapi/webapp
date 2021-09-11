from flask import Flask
from flask_restful import Resource, Api
import SERVICES.twitter_tools as tt

#Crear instancia de flask
#le damos instancia de flask a Api
app = Flask(__name__)
api = Api(app)

#La clase hello hereda de Resource
class Hello(Resource):
    def get(self, name):
        return {"hello": name}
class Search(Resource):
    def get(self, name):
        person = tt.twitter(name)
        return person

#Recurso a la API y asociación con ruta
api.add_resource(Search, '/search/<name>')
api.add_resource(Hello, '/hello/<name>')

#correr aplicación
if __name__ == '__main__':
    app.run(debug=True)

