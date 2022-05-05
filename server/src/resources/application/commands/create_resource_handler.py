from importlib.resources import Resource
from dependency_injector.wiring import Provide, inject
from resources.infraestructure.repositories.resource_respository import ResourceRepository
from shared.infraestructure.dependency_injection.app_container import AppContainer
from dependency_injector.wiring import Provide, inject


class CreateResourceHandler(object):
    @inject
    def __init__(self, resource_repository: ResourceRepository = AppContainer().container.ResourceRepository()):
        self.resource_repository = resource_repository

    def handle(self, command):
        self.resource_repository.save(command.name)
        print("handling", command.name)
