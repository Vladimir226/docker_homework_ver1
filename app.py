# app.py - a minimal flask api using flask_restful
# пример взят из документации flask
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'author': 'v.a.martynenko', 'type' : 'homework'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')