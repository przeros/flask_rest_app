from app.restControllers.clientController import *
from app.restControllers.promoterController import *
from app.restControllers.emailConfirmationTokenController import *
from app.restControllers.queryController import *
from flask import Blueprint


blueprint = Blueprint("blueprint", __name__)
blueprint.route("/", methods=["GET"])(index)

blueprint.route("/clients/", methods=["GET", "POST"])(clients)
blueprint.route("/clients/<int:id>/")(client)
blueprint.route("/clients/add/")(addClient)
blueprint.route("/clients/<int:id>/delete/", methods=["GET", "POST"])(deleteClient)
blueprint.route("/clients/<int:id>/edit/", methods=["GET", "POST"])(editClient)

blueprint.route("/promoters/", methods=["GET", "POST"])(promoters)
blueprint.route("/promoters/<int:id>/")(promoter)
blueprint.route("/promoters/add/")(addPromoter)
blueprint.route("/promoters/<int:id>/delete/", methods=["GET", "POST"])(deletePromoter)
blueprint.route("/promoters/<int:id>/edit/", methods=["GET", "POST"])(editPromoter)

blueprint.route("/emailTokens/", methods=["GET", "POST"])(emailTokens)
blueprint.route("/emailTokens/<int:id>/")(emailToken)
blueprint.route("/emailTokens/add/")(addEmailToken)
blueprint.route("/emailTokens/<int:id>/delete/", methods=["GET", "POST"])(deleteEmailToken)
blueprint.route("/emailTokens/<int:id>/edit/", methods=["GET", "POST"])(editEmailToken)

blueprint.route("/query1/", methods=["GET", "POST"])(query1)
'''blueprint.route("/query2/", methods=["GET", "POST"])(query2)'''
