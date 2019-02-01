from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import configparser

# import config
config = configparser.ConfigParser()
config.read('config.ini')

# install pymysql as MySQLdb
pymysql.install_as_MySQLdb()

# app setup
app = Flask(__name__)

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
