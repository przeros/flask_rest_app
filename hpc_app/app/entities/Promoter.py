from app.db.db import db
from app.entities.User import User


class Promoter(User):
    __tablename__ = None
    totalProvisionEarned = db.Column(db.Integer, unique=False, nullable=True)
    employmentDate = db.Column(db.DateTime, unique=False, nullable=True)
    totalTicketsSold = db.Column(db.Integer, unique=False, nullable=True)
    __mapper_args__ = {
        'polymorphic_identity': 'promoter'
    }

    def __init__(
        self,
        username,
        dateOfBirth,
        email,
        enabled,
        locked,
        staticUserId,
        totalProvisionEarned,
        employmentDate,
        totalTicketsSold,
    ):
        super().__init__(username, dateOfBirth, email, enabled, locked, staticUserId)
        self.totalProvisionEarned = totalProvisionEarned
        self.employmentDate = employmentDate
        self.totalTicketsSold = totalTicketsSold
