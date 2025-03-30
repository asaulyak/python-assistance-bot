"""
This module defines the NoteEditCommand, a CLI command that allows
users to edit existing notes in the notebook. It handles editing
both the note's title and text interactively.
"""

from prompt_toolkit import prompt
from command.command import Command
from display.paginator import Paginator
from notes import Notebook, Text, Title, Note
from execution_context import ExecutionContext
from display import StylizedElements, ColorsConstants
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
        notebook: Notebook = context.notebook

        if notebook.is_empty():
            StylizedElements.stylized_print(
                "No notes to edit. Please add a note first.",
                ColorsConstants.HIGHLIGHT_COLOR.value,
            )

            return False

        notes = notebook.to_list()

        paginator = Paginator(notes)
        note_index = paginator.show('Select a note to edit')

        if note_index is None:
            return False

        note_to_edit: Note = notebook[note_index]
        existing_title = note_to_edit.get_title().value
        existing_text = note_to_edit.get_text().value

        options = ["Title", "Text"]
        options_paginator = Paginator(options)
        option_index = options_paginator.show('Select a field to edit')

        if option_index is None:
            return False

        match option_index:
            case 0:
                new_title = prompt(message="Edit title: ", default=existing_title)
                self._update_field(note_to_edit.set_title, Title, new_title)
            case 1:
                new_text = prompt(message="Edit text: ", default=existing_text)
                self._update_field(note_to_edit.set_text, Text, new_text)

        StylizedElements.stylized_print(
            "Note was updated successfully.",
            style=ColorsConstants.SUCCESS_COLOR.value,
        )

        return False

    def _update_field(self, setter: callable, field_cls: type, value: str) -> None:
        """Helper to update a field using a setter and a field class."""
        while True:
            field = init_field(field_cls, value)
            if field and not field.is_empty():
                setter(field)
                break
