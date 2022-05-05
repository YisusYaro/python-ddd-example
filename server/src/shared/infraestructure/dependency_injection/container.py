from dependency_injector import containers, providers
from resources.infraestructure.repositories.resource_respository import ResourceRepository

from ..command_bus.command_bus import CommandBus


class Container(containers.DeclarativeContainer):

    CommandBus = providers.Factory(
        CommandBus,
    )

    ResourceRepository = providers.Factory(
        ResourceRepository,
    )
