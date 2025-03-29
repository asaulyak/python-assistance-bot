"""
This module defines the NoteDeleteCommand class, which enables users to
interactively delete a note from their notebook using a CLI interface.
"""

from typing import Tuple

from command.command import Command
from display.paginator import Paginator
from execution_context import ExecutionContext
from user_input import index_question


class NoteDeleteCommand(Command):
    """
    A command that allows users to delete a note from the notebook.
    """

    @property
    def name(self):
        return "delete-note"

    @property
    def aliases(self):
        return ["dn"]

    @property
    def description(self):
        return "Delete note"

    def run(self, _, context: ExecutionContext, __) -> Tuple[str, bool]:
        paginator = Paginator(context.notebook)
        paginator.show()

        index = index_question(
            "Type index of a note (or 'q' to cancel): ", len(context.notebook) - 1
        )

        if index is None:
            return "No notes were deleted", False

        note = context.notebook[index]
        context.notebook.delete(note)

        message = "Note deleted"

        return message, False
