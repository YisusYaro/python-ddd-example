from flask import Blueprint, Response, request

from ..application.commands.create_resource_command import \
    CreateResourceCommand

resources_controller = Blueprint('resources_controller', __name__)


@resources_controller.route("/resources", methods=['GET'])
def get_resource():
    return "Getting resource"


@resources_controller.route("/resources", methods=['POST'])
def create_resource():
    body = request.get_json()
    command = CreateResourceCommand(id=body["id"], name=body["name"])
    return Response(status=204)
