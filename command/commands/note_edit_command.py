"""
This module defines the NoteEditCommand, a CLI command that allows
users to edit existing notes in the notebook. It handles editing
both the note's title and text interactively.
"""

from prompt_toolkit import prompt
from command.command import Command
from execution_context import ExecutionContext
from display import StylizedElements, ColorsConstants
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

        note_titles = [
            f"{i + 1}. {note.get_title().value}"
            for i, note in enumerate(context.notebook)
        ]

        selected_note_str = StylizedElements.console_menu(
            "Select a note to edit:", note_titles
        )

        selected_index = int(selected_note_str.split(".")[0]) - 1

        note: Note = context.notebook[selected_index]
        existing_title = note.get_title().value
        existing_text = note.get_text().value

        field_to_edit = StylizedElements.console_menu(
            "What would you like to edit?", ["Title", "Text", "Both"]
        )

        if field_to_edit in ("Title", "Both"):
            new_title = prompt(message="Edit title: ", default=existing_title)
            self._update_field(note.set_title, Title, new_title)

        if field_to_edit in ("Text", "Both"):
            new_text = prompt(message="Edit text: ", default=existing_text)
            self._update_field(note.set_text, Text, new_text)

        StylizedElements.stylized_print(
            "Note was updated successfully.",
            style=ColorsConstants.SUCCESS_COLOR.value,
        )

        stop = False
        return stop

    def _update_field(self, setter: callable, field_cls: type, value: str) -> None:
        """Helper to update a field using a setter and a field class."""
        while True:
            field = init_field(field_cls, value)
            if field and not field.is_empty():
                setter(field)
                break
