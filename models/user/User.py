from app import database


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
