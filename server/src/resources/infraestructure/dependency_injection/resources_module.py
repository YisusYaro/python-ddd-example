from dependency_injector import providers

from shared.infraestructure.dependency_injection.app_container import AppContainer

from resources.application.commands.create_resource_handler import CreateResourceHandler
from resources.infraestructure.repositories.resource_respository import ResourceRepository


def setResourcesModule():
    AppContainer().container.CreateResourceCommand = providers.Factory(
        CreateResourceHandler,
    )

    AppContainer().container.ResourceRepository = providers.Factory(
        ResourceRepository,
    )
