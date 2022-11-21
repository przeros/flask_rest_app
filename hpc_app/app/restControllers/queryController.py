from flask import render_template, request, url_for, redirect
from app.db.db import db
from sqlalchemy.orm import Session
import time
from sqlalchemy import asc, desc, func, extract, cast, text
from sqlalchemy import create_engine
from app.entities.User import User
from app.entities.Email_Confirmation_Token import EmailConfirmationToken


dbEngine = create_engine("postgresql://hpc_app:hpc_app@db:5432/hpc_app")


def index():
    return render_template("index.html")

def query1():
    with Session(dbEngine) as session:
        startTime = time.time()

        query1 = session.query(EmailConfirmationToken.id.label("tokenId"), User.email.label("email"))\
            .join(User, EmailConfirmationToken.userId == User.id)\
            .filter(User.email.like('%@kio.pl'))

        responses = query1.all()

        tokensToUpdateIds = []
        for response in responses:
            tokensToUpdateIds.append(response[0])

        session.query(EmailConfirmationToken).filter(EmailConfirmationToken.id.in_(tokensToUpdateIds)).update(
            {"token": "KIO"}
        )
        session.query(EmailConfirmationToken).filter(EmailConfirmationToken.id.not_in(tokensToUpdateIds)).update(
            {"token": "NOT_KIO"}
        )

        session.commit()
        stopTime = time.time()
        query1_orm_time = stopTime - startTime


        startTime = time.time()
        session.execute(
            'UPDATE "EmailConfirmationToken" SET token = \'KIO\' \
                WHERE "EmailConfirmationToken".id IN (SELECT "User".id FROM "User" \
                WHERE "User".email LIKE \'%@kio.pl\');'
        )
        session.execute(
            'UPDATE "EmailConfirmationToken" SET token = \'NOT_KIO\' \
                WHERE "EmailConfirmationToken".id NOT IN (SELECT "User".id FROM "User" \
                WHERE "User".email LIKE \'%@kio.pl\');'
        )
        session.commit()
        stopTime = time.time()
        query1_sql_time = stopTime - startTime

        return render_template(
            "query1.html",
            responses=responses,
            time1=query1_orm_time,
            time2=query1_sql_time,
        )