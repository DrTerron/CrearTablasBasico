from flask import Flask, jsonify
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

#---- Crea variable para request ---
app = Flask(__name__)

#--- Configuración de la base de datos ---
basedir=os.path.dirname(os.path.realpath(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'books.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ECHO']=True

api = Api(app)

db=SQLAlchemy(app)

#---Creación de tablas ---
class Book(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    title=db.Column(db.String(80),nullable=False)
    author=db.Column(db.String(50),nullable=False)
    date_added=db.Column(db.DateTime(),default=datetime.utcnow)

    def __repr__(self) -> str:
        return self.title#super().__repr__()


@api.route('/books')
class Books(Resource):
    def get(self):
        return jsonify({"mensaje":"Hola mundo"})

    def post(self):
        pass

@api.route('/book/<int:id>')
class BookResource(Resource):
    def get(self,id):
        pass

    def put(self,id):
        pass

    def delete(self,id):
        pass

@app.shell_context_processor
def make_shell_context():
    return{
        'db':db,
        'Book':Book
    }

if __name__ == "__main__":
    app.run(debug=True)