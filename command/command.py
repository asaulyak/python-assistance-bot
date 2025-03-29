"""
This module defines the base Command class for the command-line interface.

Each specific command (e.g., add-note, edit-note, save) should inherit from this class
and implement the `run` method. The class provides a common interface for handling CLI commands
within the application.
"""

from typing import List, Tuple
from execution_context import ExecutionContext


class Command:
    """
    Abstract base class for all CLI commands.

    Subclasses must implement:
        - name: the primary command keyword.
        - aliases: alternative command keywords.
        - description: a brief explanation of the command.
        - run: method that executes the command's logic.

    Attributes:
        name (str): Command keyword used to invoke this command.
        aliases (list[str]): Alternative keywords for the command.
        description (str): Description shown in help or command listings.
    """

    @property
    def name(self):
        """Returns a list of alias names for the command."""
        return "empty"

    @property
    def aliases(self):
        """Returns a list of alias names for the command."""
        return []

    @property
    def description(self):
        """Returns the description of the command."""
        return "default description"

    def run(
        self, args: list[str], context: ExecutionContext, commands: List
    ) -> Tuple[str, bool]:
        """
        Executes the command logic.

        Args:
            args (list[str]): Arguments passed to the command.
            context (ExecutionContext): The application state.
            commands (list): List of all available commands (useful for help or suggestions).

        Returns:
            Tuple[str, bool]: A tuple containing a message and a stop flag.
                              If stop is True, the CLI will exit after execution.
        """
        pass
