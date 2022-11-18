from app.db.db import db


class StaticEmailConfirmationToken(db.Model):
    __tablename__ = "StaticEmailConfirmationToken"

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    timeToExpire = db.Column(db.Integer, unique=False, nullable=True)

    def __init__(
        self,
        timeToExpire,
    ):
        self.timeToExpire = timeToExpire
