from flask import Flask
from Flask_CRUD_APP.users.routes import users

app = Flask(__name__)
app.register_blueprint(users)