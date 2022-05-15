from resources.infrastructure.repositories.resource_respository import ResourceRepository
from shared.infrastructure.dependency_injection.app import App
from resources.domain.factory import Factory


class CreateResourceHandler(object):
    def __init__(self, resource_repository: ResourceRepository = App().container.ResourceRepository()):
        self.resource_repository = resource_repository

    def handle(self, command):
        resource = Factory.create(id=command.id, name=command.name)

        resource.handleCreation()
        
        self.resource_repository.save(resource)

        resource.commit()
