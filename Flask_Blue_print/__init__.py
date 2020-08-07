from Flask_CRUD_APP.config import config

app = Flask(__name__)
app.config.from_object(config)
