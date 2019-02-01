from app import app
from models.user import *


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/user/<int:user_id>')
def user(user_id):
    selected_user = User.query.filter_by(id=user_id).first_or_404()
    return str(selected_user.username)
