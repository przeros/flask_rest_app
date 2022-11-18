from app.db.db import db


class StaticUser(db.Model):
    __tablename__ = "StaticUser"

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    minAge = db.Column(db.Integer, unique=False, nullable=True)
    defaultBanLength = db.Column(db.Integer, unique=False, nullable=True)
    provisionRate = db.Column(db.Integer, unique=False, nullable=True)

    def __init__(
        self,
        minAge,
        defaultBanLength,
        provisionRate,
    ):
        self.minAge = minAge
        self.defaultBanLength = defaultBanLength
        self.provisionRate = provisionRate
