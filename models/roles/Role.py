from app import database


class Role(database.Model):

    # model settings
    __tablename__ = 'Roles'

    # model setup
    id = database.Column(database.BIGINT, primary_key=True)
    short = database.Column(database.String(16), unique=True, nullable=False)

    def __repr__(self):
        return '<User[ID: %r | short: %r]>' % (self.id, self.short)
