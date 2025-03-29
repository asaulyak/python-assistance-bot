"""This module defines the NoteAddCommand class, which allows users to add new notes
to the notebook within the CLI assistant."""

from typing import Tuple

from command.command import Command
from execution_context import ExecutionContext
from field import init_field
from notes import Title, Text, Note


class NoteAddCommand(Command):
    """
    A command class responsible for adding a new note to the notebook.
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

    def run(self, _, context: ExecutionContext, __) -> Tuple[str, bool]:
        title = None
        text = None

        while not title or title.is_empty():
            title = init_field(Title, input("Title: "))

        while not text:
            text = init_field(Text, input("Text: "))

        note = Note(title, text)

        context.notebook.add(note)

        return "Note added", False
