from flask import render_template, request, url_for, redirect
from app.db.db import db
from app.entities.Email_Confirmation_Token import EmailConfirmationToken
import datetime
from sqlalchemy import asc

def emailTokens():
    if request.method == "POST":
        creationDate = request.form["creationDate"]
        confirmationDate = request.form["confirmationDate"]
        expirationDate = request.form["expirationDate"]
        token = request.form["token"]
        userId = request.form["userId"]
        newEmailToken = EmailConfirmationToken(
            creationDate=creationDate,
            confirmationDate=confirmationDate,
            expirationDate=expirationDate,
            token=token,
            userId=userId,
            staticEmailConfirmationTokenId=1,
        )
        db.session.add(newEmailToken)
        db.session.commit()

        return redirect(url_for("blueprint.emailTokens"))
    else:
        emailTokens = EmailConfirmationToken.query.order_by(asc(EmailConfirmationToken.id)).all()
        return render_template("emailTokens.html", emailTokens=emailTokens)


def emailToken(id):
    emailToken = EmailConfirmationToken.query.get_or_404(id)
    return render_template("emailToken.html", emailToken=emailToken)


def addEmailToken():
    return render_template("addEmailToken.html")


def deleteEmailToken(id):
    emailToken = EmailConfirmationToken.query.get_or_404(id)
    db.session.delete(emailToken)
    db.session.commit()
    return redirect(url_for("blueprint.emailTokens"))


def editEmailToken(id):
    oldEmailToken = EmailConfirmationToken.query.get_or_404(id)
    if request.method == "POST":

        try:
            oldEmailToken.confirmationDate = request.form["confirmationDate"]
        except:
            pass

        try:
            oldEmailToken.expirationDate = request.form["expirationDate"]
        except:
            pass

        try:
            oldEmailToken.token = request.form["token"]
        except:
            pass

        db.session.add(oldEmailToken)
        db.session.commit()

        return redirect(url_for("blueprint.emailTokens"))
    else:
        return render_template("editEmailToken.html", oldEmailToken=oldEmailToken)

