from flask import render_template, request, url_for, redirect
from app.db.db import db
from app.entities.Client import Client
import datetime
from sqlalchemy import asc

def clients():
    if request.method == "POST":
        username = request.form["username"]
        dateOfBirth = request.form["dateOfBirth"]
        email = request.form["email"]
        favoriteMusic = request.form["favoriteMusic"]
        favoriteEventType = request.form["favoriteEventType"]
        newClient = Client(
            username=username,
            dateOfBirth=dateOfBirth,
            email=email,
            enabled=True,
            locked=False,
            staticUserId=1,
            favoriteMusic=favoriteMusic,
            favoriteEventType=favoriteEventType,
            registrationDate=datetime.datetime.now(),
        )
        db.session.add(newClient)
        db.session.commit()

        return redirect(url_for("blueprint.clients"))
    else:
        clients = Client.query.order_by(asc(Client.id)).all()
        return render_template("clients.html", clients=clients)


def client(id):
    client = Client.query.get_or_404(id)
    return render_template("client.html", client=client)


def addClient():
    return render_template("addClient.html")


def deleteClient(id):
    client = Client.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for("blueprint.clients"))


def editClient(id):
    oldClient = Client.query.get_or_404(id)
    if request.method == "POST":

        try:
            oldClient.username = request.form["username"]
        except:
            pass

        try:
            oldClient.email = request.form["email"]
        except:
            pass

        try:
            oldClient.favoriteMusic = request.form["favoriteMusic"]
        except:
            pass

        try:
            oldClient.favoriteEventType = request.form["favoriteEventType"]
        except:
            pass

        db.session.add(oldClient)
        db.session.commit()

        return redirect(url_for("blueprint.clients"))
    else:
        return render_template("editClient.html", oldClient=oldClient)

