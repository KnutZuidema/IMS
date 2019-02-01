from app import app
from models.user import *
from flask import render_template


###########################################
# MAIN ROUTES                             #
###########################################
@app.route('/')
def index():
    return render_template('index.html')


###########################################
# TEST ROUTES                             #
###########################################
@app.route('/user/<int:user_id>')
def user(user_id):
    selected_user = User.query.filter_by(id=user_id).first_or_404()
    return str(selected_user.username)
