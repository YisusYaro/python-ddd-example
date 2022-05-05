from ..dependency_injection import app_container


class CommandBus(object):
    def execute(self, command):
        command_handler = app_container.AppContainer().container.__getattribute__(
            command.__class__.__name__)()
        command_handler.handle(command)
