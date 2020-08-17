from flask_sqlalchemy import SQLAlchemy
import psycopg2
from psycopg2 import sql
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
print (db)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(16), index=True, unique=True)
    lastname = db.Column(db.String(16), index=True, unique=True)
    email = db.Column(db.String(16), index=True, unique=True)
    password = db.Column(db.String(16), index=True, unique=True)

    def __repr__(self):
        return '<User {0}>'.format(self.name)

    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.name,
            'laststname': self.name,
            'email': self.name,
            'paswword': self.name,
            
        }
