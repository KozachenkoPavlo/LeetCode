import importlib
import inspect
from typing import Type

from cli.commands.command import Command

COMMANDS_PACKAGE = "cli.commands"
ALIASES = {
    "create": "create_package_command",
}


class UnknownCommandError(Exception):
    pass


def load_command(name: str) -> Command:
    module_name = ALIASES.get(name, name)

    try:
        module = importlib.import_module(f"{COMMANDS_PACKAGE}.{module_name}")
    except ModuleNotFoundError as error:
        raise UnknownCommandError(f"No command named '{module_name}'") from error

    command_class = _find_command_class(module)
    command = command_class.create()

    return command


def _find_command_class(module) -> Type[Command]:
    for _, obj in inspect.getmembers(module, inspect.isclass):
        if issubclass(obj, Command) and obj is not Command and obj.__module__ == module.__name__:
            return obj

    raise UnknownCommandError(f"Module '{module.__name__}' does not define a Command")
