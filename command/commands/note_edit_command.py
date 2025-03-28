"""
This module defines the NoteEditCommand, a CLI command that allows
users to edit existing notes in the notebook. It handles editing
both the note's title and text interactively.
"""

from typing import Tuple
from command.command import Command
from execution_context import ExecutionContext
from display.paginator import Paginator
from display import StylizedElements, ColorsConstants
from user_input import index_question, yes_no_question
from notes import Text, Title, Note
from field import init_field


class NoteEditCommand(Command):
    """
    A command class that allows users to edit an existing note in the notebook.
    """

    @property
    def name(self):
        return "edit-note"

    @property
    def aliases(self):
        return ["edn"]

    @property
    def description(self):
        return "Edit note"

    def run(self, _, context: ExecutionContext, __) -> bool:
        if not context.notebook:
            StylizedElements.stylized_print(
                "No notes to edit. Please add a note first.",
                ColorsConstants.HIGHLIGHT_COLOR.value,
            )

            return False

        paginator = Paginator(context.notebook)

        paginator.show()

        index = index_question(
            "Type an index of a note to edit (or 'q' to cancel): ",
            max_index=len(context.notebook) - 1,
        )

        note: Note = context.notebook[index]

        if yes_no_question("Do you want to edit the title?"):
            self._update_field(note.set_title, Title, "Enter new title: ")

        if yes_no_question("Do you want to edit the text?"):
            self._update_field(note.set_text, Text, "Enter new text: ")

        StylizedElements.stylized_print(
            "Note was updated successfully.", style=ColorsConstants.SOFT_COLOR.value
        )

        return False

    def _update_field(self, setter: callable, field_cls: type, prompt: str) -> None:
        """Helper to update a field using a setter and a field class."""
        while True:
            raw_value = input(prompt)
            field = init_field(field_cls, raw_value)
            if field and not field.is_empty():
                setter(field)
                break
