from flask import Blueprint

resources_controller = Blueprint('resources_controller', __name__)

@resources_controller.route("/resources", methods=['GET'])
def get_resource():
    return "Getting resource"

@resources_controller.route("/resources", methods=['POST'])
def create_resource():
    return "Creating resource"