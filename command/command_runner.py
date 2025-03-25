import importlib
import pkgutil
from . import commands
import inspect
from .command import Command
import difflib


class CommandRunner:
    def __init__(self):
        self.commands = self.__load_commands()


    def find_command(self, name: str) -> Command | None:
        command = self.commands.get(name)

        return command if command else None


    def find_suggested_command(self, name) -> str | None:
        matches = difflib.get_close_matches(name, self.commands.keys(), n=1, cutoff=0.6)

        match = matches[0] if matches else None

        command = self.commands.get(match)

        return match if command else None


    def __load_commands(self) -> dict[str, Command]:
        """
        Import all modules from `commands` that match the pattern `*_command.py`
        and return a dictionary of command names to their functions.
        """
        imported_commands = {}

        for finder, module_name, ispkg in pkgutil.iter_modules(commands.__path__):
            if module_name.endswith("_command"):
                full_module_name = f"{commands.__name__}.{module_name}"
                try:
                    module = importlib.import_module(full_module_name)

                    # Find the class that inherits from Command
                    command_class = None
                    for name, obj in inspect.getmembers(module, inspect.isclass):
                        if issubclass(obj, Command) and obj is not Command:
                            command_class = obj
                            break

                    if command_class:
                        command_instance = command_class()
                        imported_commands[command_instance.name] = command_instance

                        for alias in command_instance.aliases:
                            if imported_commands.get(alias):
                                raise ValueError(f'Alias {alias} shadows already existing command. Pick another alias for the command {command_instance.name}')

                            imported_commands[alias] = command_instance
                    else:
                        print(f"Module {full_module_name} does not define a subclass of Command.")
                except Exception as e:
                    print(f"Failed to import {full_module_name}: {e}")

        return imported_commands
