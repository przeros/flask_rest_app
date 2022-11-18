from app.db.db import db


class EmailConfirmationToken(db.Model):
    __tablename__ = "EmailConfirmationToken"

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    creationDate = db.Column(db.DateTime, unique=False, nullable=True)
    confirmationDate = db.Column(db.DateTime, unique=False, nullable=True)
    expirationDate = db.Column(db.DateTime, unique=False, nullable=True)
    token = db.Column(db.String(128), unique=False, nullable=True)
    userId = db.Column(db.Integer, db.ForeignKey("User.id"))
    staticEmailConfirmationTokenId = db.Column(db.Integer, db.ForeignKey("StaticEmailConfirmationToken.id"))

    def __init__(
        self,
        creationDate,
        confirmationDate,
        expirationDate,
        token,
        userId,
        staticEmailConfirmationTokenId,
    ):
        self.creationDate = creationDate
        self.confirmationDate = confirmationDate
        self.expirationDate = expirationDate
        self.token = token
        self.userId = userId
        self.staticEmailConfirmationTokenId = staticEmailConfirmationTokenId
