from app.restControllers.clientController import *
from app.restControllers.promoterController import *
from app.restControllers.emailConfirmationTokenController import *
from app.restControllers.queryController import *
from flask import Blueprint


blueprint = Blueprint("blueprint", __name__)
'''blueprint.route("/", methods=["GET"])(index)

blueprint.route("/clients/", methods=["GET", "POST"])(clients)
blueprint.route("/clients/<int:id>/")(client)
blueprint.route("/clients/add/")(addClient)
blueprint.route("/clients/<int:id>/delete/", methods=["GET", "POST"])(deleteClient)
blueprint.route("/clients/<int:id>/edit/", methods=["GET", "POST"])(editClient)
blueprint.route("/query1/", methods=["GET", "POST"])(query1)
blueprint.route("/query2/", methods=["GET", "POST"])(query2)'''
