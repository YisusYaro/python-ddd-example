from dependency_injector import containers, providers
from resources.infraestructure.repositories.resource_respository import ResourceRepository

from ..command_bus.command_bus import CommandBus
from ..query_bus.query_bus import QueryBus


class Container(containers.DeclarativeContainer):

    CommandBus = providers.Factory(
        CommandBus,
    )

    QueryBus = providers.Factory(
        QueryBus,
    )

    ResourceRepository = providers.Factory(
        ResourceRepository,
    )
