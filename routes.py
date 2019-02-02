from app import app
from models.user import *
from flask import render_template, redirect, flash, url_for
from forms import *


###########################################
# MAIN ROUTES                             #
###########################################
@app.route('/')
def index():
    return redirect(url_for('sign_in'))


@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    # set from
    form = SignInForm()

    # check if from was submit
    if form.validate_on_submit():

        # get selected user by email
        selected_user = User.query.filter_by(email=form.email.data).first()

        # check if user not exist
        if selected_user is None:

            # return error and redirect
            flash('Incorrect access data. Please try again.'.format(form.email.data, form.password.data))
            return redirect(url_for('sign_in'))

        # return success and redirect
        flash('Login requested for email {}, password={}'.format(form.email.data, form.password.data))
        return redirect(url_for('sign_in'))

    # render template
    return render_template('sign_in.html', title='Sign In', form=form)


###########################################
# TEST ROUTES                             #
###########################################
@app.route('/user/<int:user_id>')
def user(user_id):
    selected_user = User.query.filter_by(id=user_id).first_or_404()
    return str(selected_user.username)
