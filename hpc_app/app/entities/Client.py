from app.db.db import db
from app.entities.User import User


class Client(User):
    __tablename__ = None
    favoriteMusic = db.Column(db.String(128), unique=False, nullable=True)
    favoriteEventType = db.Column(db.String(128), unique=False, nullable=True)
    registrationDate = db.Column(db.DateTime, unique=False, nullable=True)
    __mapper_args__ = {
        'polymorphic_identity': 'client'
    }

    def __init__(
        self,
        username,
        dateOfBirth,
        email,
        enabled,
        locked,
        staticUserId,
        favoriteMusic,
        favoriteEventType,
        registrationDate,
    ):
        super().__init__(username, dateOfBirth, email, enabled, locked, staticUserId)
        self.favoriteMusic = favoriteMusic
        self.favoriteEventType = favoriteEventType
        self.registrationDate = registrationDate
