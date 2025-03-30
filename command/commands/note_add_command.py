"""This module defines the NoteFindCommand class, which allows users to search for notes
in the notebook either by their title or by a specific tag.
Results are displayed in a stylized format using the StylistElements utility."""

from typing import List

from command.command import Command
from display import StylizedElements, ColorsConstants
from execution_context import ExecutionContext
from field import init_field
from notes import Title, Text, Note


class NoteAddCommand(Command):
    """A command that allows users to add a new note to the notebook.

    This command interactively prompts the user to enter a title and text for the note.
    It validates that both fields are non-empty before creating the Note instance.
    Once created, the note is added to the notebook within the current execution context.
    """

    @property
    def name(self):
        return "add-note"

    @property
    def aliases(self):
        return ["an"]

    @property
    def description(self):
        return "Add a note"

    def run(self, args: list[str], context: ExecutionContext, commands: List) -> bool:
        title = None
        text = None

        while not title or title.is_empty():
            title = init_field(
                Title,
                StylizedElements.stylized_input(
                    "Title: ", ColorsConstants.INPUT_COLOR.value
                ),
            )

        while not text:
            text = init_field(
                Text,
                StylizedElements.stylized_input(
                    "Text: ", ColorsConstants.INPUT_COLOR.value
                ),
            )

        note_to_add = Note(title, text)

        context.notebook.add(note_to_add)

        StylizedElements.stylized_print(
            "Note added", style=ColorsConstants.SUCCESS_COLOR.value
        )
        stop = False

        return stop
