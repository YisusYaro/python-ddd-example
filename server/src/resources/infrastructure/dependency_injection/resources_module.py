from dependency_injector import providers

from shared.infrastructure.dependency_injection.app import App

from resources.application.commands.create_resource_handler import CreateResourceHandler
from resources.application.queries.get_resource_handler import GetResourceHandler
from resources.infrastructure.repositories.resource_respository import ResourceRepository
from resources.application.events.resource_created_handler import ResourceCreatedHandler


def setCommands():
    App().container.CreateResourceCommand = providers.Factory(
        CreateResourceHandler,
    )


def setQueries():
    App().container.GetResourceQuery = providers.Factory(
        GetResourceHandler,
    )


def setEvents():
    App().container.ResourceCreatedEvent = providers.Factory(
        ResourceCreatedHandler,
    )


def setApplication():
    setCommands()
    setQueries()
    setEvents()


def setInfrastructure():
    App().container.ResourceRepository = providers.Singleton(
        ResourceRepository,
    )


def setResourcesModule():
    setApplication()
    setInfrastructure()
