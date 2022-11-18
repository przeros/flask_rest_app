from app.db.db import db


class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    userType = db.Column(db.String(128), unique=False, nullable=False)
    username = db.Column(db.String(128), unique=True, nullable=True)
    dateOfBirth = db.Column(db.DateTime, unique=False, nullable=True)
    email = db.Column(db.String(128), unique=False, nullable=True)
    enabled = db.Column(db.Boolean, unique=False, nullable=True)
    locked = db.Column(db.Boolean, unique=False, nullable=True)
    staticUserId = db.Column(db.Integer, db.ForeignKey("StaticUser.id"))
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': userType,
    }

    def __init__(
        self,
        username,
        dateOfBirth,
        email,
        enabled,
        locked,
        staticUserId,
    ):
        self.username = username
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.enabled = enabled
        self.locked = locked
        self.staticUserId = staticUserId
