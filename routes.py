from app import app
from models.user import *
from flask import render_template, redirect, flash, url_for
from forms import *


###########################################
# MAIN ROUTES                             #
###########################################
@app.route('/')
def index():
    return redirect(url_for('signin'))


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        flash('Login requested for email {}, password={}'.format(form.email.data, form.password.data))
        return redirect(url_for('signin'))
    return render_template('signin.html', title='Sign In', form=form)


###########################################
# TEST ROUTES                             #
###########################################
@app.route('/user/<int:user_id>')
def user(user_id):
    selected_user = User.query.filter_by(id=user_id).first_or_404()
    return str(selected_user.username)
