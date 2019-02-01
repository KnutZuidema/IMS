from app import app
from models.user import *
from flask import render_template, redirect


###########################################
# MAIN ROUTES                             #
###########################################
@app.route('/')
def index():
    return redirect('/signin')


@app.route('/signin')
def signin():
    return render_template('signin.html')


###########################################
# TEST ROUTES                             #
###########################################
@app.route('/user/<int:user_id>')
def user(user_id):
    selected_user = User.query.filter_by(id=user_id).first_or_404()
    return str(selected_user.username)
