from typing import List

from command.command import Command
from display import StylizedElements, ColorsConstants
from execution_context import ExecutionContext
from field import init_field
from notes import Title, Text, Note


class NoteAddCommand(Command):
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
