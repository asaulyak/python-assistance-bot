"""
This module defines the AddTagNoteCommand class, which provides functionality
to add a tag to a specific note in the user's notebook using a command-line interface.
"""

from typing import Tuple

from command.command import Command
from display.paginator import Paginator
from execution_context import ExecutionContext
from field import init_field
from notes import Tag
from user_input import index_question


class AddTagNoteCommand(Command):
    """
    A command that allows the user to assign a tag to a specific note.
    """

    @property
    def name(self):
        return "add-tag-note"

    @property
    def aliases(self):
        return ["tag"]

    @property
    def description(self):
        return "Add tag to a note"

    def run(self, _, context: ExecutionContext, __) -> Tuple[str, bool]:
        paginator = Paginator(context.notebook)

        paginator.show()

        index = index_question(
            "Type an index of a note to edit (or 'q' to cancel): ",
            max_index=len(context.notebook) - 1,
        )

        if index is None:
            return "No tags added", False

        while True:
            tag = init_field(Tag, input("Provide a tag: "))

            if tag and not tag.is_empty():
                break

        note = context.notebook[index]

        note.add_tag(tag)

        message = f"Added tag to note: {note}"

        return message, False
