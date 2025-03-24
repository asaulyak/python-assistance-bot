import importlib
import pkgutil
from . import commands
import inspect
from .command import Command
import difflib


class CommandParser:
    def __init__(self):
        self.commands = self.__load_commands()

    def parse_command(self, user_input):
        if not user_input:
            return 'not_a_command', []

        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()

        return cmd, *args


    def find_command(self, name: str) -> Command | None:
        command = self.commands.get(name)

        return command if command else None



    def find_alias_command(self, alias) -> Command | None:
        for name, command in self.commands.items():
            if alias in command.aliases:
                return command

        return None


    def find_suggested_command(self, name) -> Command | None:
        matches = difflib.get_close_matches(name, self.commands, n=1, cutoff=0.6)

        match = matches[0] if matches else None

        command = self.commands.get(match)

        return command if command else None


    def __load_commands(self):
        """
        Import all modules from `commands` that match the pattern `*.command.py`
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
                    else:
                        print(f"Module {full_module_name} does not define a subclass of Command.")
                except Exception as e:
                    print(f"Failed to import {full_module_name}: {e}")

        return imported_commands
