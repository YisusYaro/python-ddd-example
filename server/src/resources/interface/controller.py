from flask import Blueprint, Response, request

from ..application.commands.create_resource_command import \
    CreateResourceCommand
from shared.infraestructure.dependency_injection.app_container import AppContainer

resources_controller = Blueprint('resources_controller', __name__)
command_bus = AppContainer().container.CommandBus()

@resources_controller.route("/resources", methods=['GET'])
def get_resource():
    return "Getting resource"


@resources_controller.route("/resources", methods=['POST'])
def create_resource():
    body = request.get_json()
    command = CreateResourceCommand(id=body["id"], name=body["name"])
    command_bus.execute(command)
    return Response(status=204)
