from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import dirname, abspath, join
import pymysql
import configparser

# import config
config = configparser.ConfigParser()
config.read('config.ini')

# install pymysql as MySQLdb
pymysql.install_as_MySQLdb()

# setup directories
ROOT_DIR = dirname(abspath(__file__))
STATIC_DIR = join(ROOT_DIR, 'static')
TEMPLATES_DIR = join(ROOT_DIR, 'templates')

# app setup
app = Flask(__name__, template_folder=TEMPLATES_DIR)

# set flask config
for key, setting in config['flask'].items():
    app.config[str(key).upper()] = setting

# set database uri
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + str(config['database']['user']) + ':' + str(
    config['database']['password']) + '@' + str(config['database']['host']) + ':' + str(
    config['database']['port']) + '/' + str(config['database']['name']) + ''

# get database
database = SQLAlchemy(app)
# run app if main
if __name__ == "__main__":
    app.run()

# import routes
from routes import *
