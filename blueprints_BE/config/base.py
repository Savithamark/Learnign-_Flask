# flake8: noqa
from .env import ENV_BOOL, ENV_STR, ABS_PATH

DEBUG = ENV_BOOL('DEBUG', False)
SECRET_KEY = ENV_STR('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/mydb'
SQLALCHEMY_TRACK_MODIFICATIONS = False
