from dependency_injector import containers, providers
from resources.infrastructure.repositories.resource_respository import ResourceRepository

from ..command_bus.command_bus import CommandBus
from ..query_bus.query_bus import QueryBus
from ..event_bus.event_bus import EventBus


class Container(containers.DeclarativeContainer):

    CommandBus = providers.Factory(
        CommandBus,
    )

    QueryBus = providers.Factory(
        QueryBus,
    )

    EventBus = providers.Factory(
        EventBus,
    )

    ResourceRepository = providers.Factory(
        ResourceRepository,
    )
