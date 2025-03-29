"""
This module defines the NoteShowAllCommand class, which provides functionality to display all notes
stored in the notebook within the current execution context.
"""


from command.command import Command
from display import StylizedElements
from execution_context import ExecutionContext


class NoteShowAllCommand(Command):
    """A command class to display all notes in the user's notebook.

    Attributes:
        name (str): The command keyword used to invoke this action.
        aliases (list[str]): Alternate keywords for the command.
        description (str): A short explanation of the command’s functionality."""

    @property
    def name(self):
        return "all-notes"

    @property
    def aliases(self):
        return ["alln"]

    @property
    def description(self):
        return "Show all notes"

    def run(self, _, context: ExecutionContext, __) -> bool:
        message = str(context.notebook)

        StylizedElements.stylized_print(message)

        return False
