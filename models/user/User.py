from app import database
from werkzeug.security import generate_password_hash, check_password_hash


class User(database.Model):

    # model settings
    __tablename__ = 'Users'

    # model setup
    id = database.Column(database.BIGINT, primary_key=True)
    username = database.Column(database.String(32), unique=True, nullable=False)
    surname = database.Column(database.String(64), nullable=False)
    first_name = database.Column(database.String(64), nullable=False)
    email = database.Column(database.String(132), unique=True, nullable=False)
    password = database.Column(database.String(256), nullable=False)

    def __repr__(self):
        return '<User[ID: %r | username: %r]>' % (self.id, self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
