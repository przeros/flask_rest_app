from flask import render_template, request, url_for, redirect
from app.db.db import db
from app.entities.Promoter import Promoter
import datetime
from sqlalchemy import asc

def promoters():
    if request.method == "POST":
        username = request.form["username"]
        dateOfBirth = request.form["dateOfBirth"]
        email = request.form["email"]
        totalProvisionEarned = request.form["totalProvisionEarned"]
        totalTicketsSold = request.form["totalTicketsSold"]
        employmentDate = request.form["employmentDate"]
        newPromoter = Promoter(
            username=username,
            dateOfBirth=dateOfBirth,
            email=email,
            enabled=True,
            locked=False,
            staticUserId=1,
            totalProvisionEarned=totalProvisionEarned,
            totalTicketsSold=totalTicketsSold,
            employmentDate=employmentDate,
        )
        db.session.add(newPromoter)
        db.session.commit()

        return redirect(url_for("blueprint.promoters"))
    else:
        promoters = Promoter.query.order_by(asc(Promoter.id)).all()
        return render_template("promoters.html", promoters=promoters)


def promoter(id):
    promoter = Promoter.query.get_or_404(id)
    return render_template("promoter.html", promoter=promoter)


def addPromoter():
    return render_template("editPromoter.html")


def deletePromoter(id):
    promoter = Promoter.query.get_or_404(id)
    db.session.delete(promoter)
    db.session.commit()
    return redirect(url_for("blueprint.promoters"))


def editPromoter(id):
    oldPromoter = Promoter.query.get_or_404(id)
    if request.method == "POST":

        try:
            oldPromoter.username = request.form["username"]
        except:
            pass

        try:
            oldPromoter.email = request.form["email"]
        except:
            pass

        try:
            oldPromoter.totalProvisionEarned = request.form["totalProvisionEarned"]
        except:
            pass

        try:
            oldPromoter.totalTicketsSold = request.form["totalTicketsSold"]
        except:
            pass

        db.session.add(oldPromoter)
        db.session.commit()

        return redirect(url_for("blueprint.promoters"))
    else:
        return render_template("editPromoter.html", oldPromoter=oldPromoter)