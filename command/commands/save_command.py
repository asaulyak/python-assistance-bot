"""This module defines the SaveCommand class for persisting the current application state.

The SaveCommand is responsible for invoking the data persistence layer to save the
current execution context (including contacts, notes, etc.) to a storage medium."""

from command.command import Command
from execution_context import ExecutionContext
from persistence import save_data


class SaveCommand(Command):
    """
    Command to save the current application state to persistent storage.
    """

    @property
    def name(self):
        return "save"

    @property
    def aliases(self):
        return ["s"]

    @property
    def description(self):
        return "Save current state to the storage"

    def run(self, _, context: ExecutionContext, __):
        message = "Data successfully saved"
        stop = False

        save_data(context)

        return message, stop
