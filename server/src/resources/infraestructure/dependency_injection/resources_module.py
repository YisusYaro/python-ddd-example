from dependency_injector import providers

from shared.infraestructure.dependency_injection.app import App

from resources.application.commands.create_resource_handler import CreateResourceHandler
from resources.infraestructure.repositories.resource_respository import ResourceRepository


def setResourcesModule():
    App().container.CreateResourceCommand = providers.Factory(
        CreateResourceHandler,
    )

    App().container.ResourceRepository = providers.Singleton(
        ResourceRepository,
    )
