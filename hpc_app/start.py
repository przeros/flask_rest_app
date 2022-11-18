from app import app
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import relationship
from app.db.db import db
from app.entities.User import User
from app.entities.Client import Client
from app.entities.Promoter import Promoter
from app.entities.Static_User import StaticUser
from app.entities.StaticEmailConfirmationToken import StaticEmailConfirmationToken
from app.entities.Email_Confirmation_Token import EmailConfirmationToken
from datetime import datetime
from app.routes.routes import blueprint
import pandas as pd


def createDb():
    with app.app_context():
        db.drop_all()
    with app.app_context():
        db.create_all()
        db.session.commit()


def setupData():
    with app.app_context():
        db.session.add(
            StaticUser(
                minAge = 16,
                defaultBanLength = 50,
                provisionRate = 10,
            )
        )

        db.session.add(
            StaticEmailConfirmationToken(
                timeToExpire = 100,
            )
        )

        db.session.add(
            StaticEmailConfirmationToken(
                timeToExpire=0,
            )
        )

        db.session.commit()

        db.session.add(
            Client(
                username = 'Kras123',
                dateOfBirth = datetime.strptime("Jun 3 2006", "%b %d %Y"),
                email = 'kras123@gmail.com',
                enabled = True,
                locked = False,
                staticUserId = 1,
                favoriteMusic = 'jazz',
                favoriteEventType = 'wedding',
                registrationDate = datetime.strptime("Jan 12 2016", "%b %d %Y"),
            )
        )

        db.session.add(
            Promoter(
                username = 'bompur1',
                dateOfBirth = datetime.strptime("Sep 15 2007", "%b %d %Y"),
                email = 'bompur@gmail.com',
                enabled = True,
                locked = False,
                staticUserId = 1,
                totalProvisionEarned = 90,
                employmentDate = datetime.strptime("Jan 4 2011", "%b %d %Y"),
                totalTicketsSold = 6,
            )
        )

        db.session.commit()

        db.session.add(
            EmailConfirmationToken(
                creationDate = datetime.strptime("Jan 4 2002", "%b %d %Y"),
                confirmationDate = datetime.strptime("Jan 4 2003", "%b %d %Y"),
                expirationDate = datetime.strptime("Jan 4 2007", "%b %d %Y"),
                token = 'pljd',
                userId = 1,
                staticEmailConfirmationTokenId = 1,
            )
        )

        db.session.commit()

def loadDataFromCsv():
    clientsCsv = pd.read_csv(r"./data/client.csv", delimiter=",")
    global clientsFormated
    clientsFormated = pd.DataFrame(
        clientsCsv,
        columns=['username', 'dateOfBirth', 'email', 'enabled', 'locked', 'staticUserId', 'favoriteMusic',
                 'favoriteEventType', 'registrationDate']
    )

    promotersCsv = pd.read_csv(r"./data/promoter.csv", delimiter=",")
    global promotersFormated
    promotersFormated = pd.DataFrame(
        promotersCsv,
        columns=['username', 'dateOfBirth', 'email', 'enabled', 'locked', 'staticUserId', 'totalProvisionEarned',
                 'employmentDate', 'totalTicketsSold']
    )

    emailTokensCsv = pd.read_csv(r"./data/emailConfirmationToken.csv", delimiter=",")
    global emailTokensFormated
    emailTokensFormated = pd.DataFrame(
        emailTokensCsv,
        columns=['creationDate', 'confirmationDate', 'expirationDate', 'token', 'userId', 'staticEmailConfirmationTokenId']
    )

def loadClientsToDb():
    with app.app_context():
        for index, row in clientsFormated.iterrows():
            db.session.add(
                Client(
                    username=row['username'],
                    dateOfBirth=row['dateOfBirth'],
                    email=row['email'],
                    enabled=bool(row['enabled']),
                    locked=bool(row['locked']),
                    staticUserId=row['staticUserId'],
                    favoriteMusic=row['favoriteMusic'],
                    favoriteEventType=row['favoriteEventType'],
                    registrationDate=row['registrationDate'],
                )
            )
        db.session.commit()

def loadPromotersToDb():
    with app.app_context():
        for index, row in promotersFormated.iterrows():
            db.session.add(
                Promoter(
                    username=row['username'],
                    dateOfBirth=row['dateOfBirth'],
                    email=row['email'],
                    enabled=bool(row['enabled']),
                    locked=bool(row['locked']),
                    staticUserId=row['staticUserId'],
                    totalProvisionEarned=row['totalProvisionEarned'],
                    employmentDate=row['employmentDate'],
                    totalTicketsSold=row['totalTicketsSold'],
                )
            )
        db.session.commit()

def loadEmailConfirmationTokensToDb():
    with app.app_context():
        for index, row in emailTokensFormated.iterrows():
            db.session.add(
                EmailConfirmationToken(
                    creationDate=row['creationDate'],
                    confirmationDate=row['confirmationDate'],
                    expirationDate=row['expirationDate'],
                    token=row['token'],
                    userId=row['userId'],
                    staticEmailConfirmationTokenId=row['staticEmailConfirmationTokenId'],
                )
            )
        db.session.commit()


app = Flask(__name__, template_folder="app/frontend")
app.config.from_object("app.config.Config")
db.init_app(app)
app.register_blueprint(blueprint, url_prefix="/")
migrate = Migrate(app, db)
createDb()
setupData()
loadDataFromCsv()
loadClientsToDb()
loadPromotersToDb()
loadEmailConfirmationTokensToDb()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
