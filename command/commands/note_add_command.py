from typing import List

from command.command import Command
from display import StylizedElements
from execution_context import ExecutionContext
from field import init_field
from notes import Title, Text, Note


class NoteAddCommand(Command):
    @property
    def name(self):
        return 'add-note'


    @property
    def aliases(self):
        return ['an']


    @property
    def description(self):
        return 'Add a note'

    def run(self, args: list[str], context: ExecutionContext, commands: List) -> bool:
        title = None
        text = None

        while not title or title.is_empty():
            title = init_field(Title, input('Title: '))

        while not text:
            text = init_field(Text, input('Text: '))

        note = Note(title, text)

        context.notebook.add(note)

        StylizedElements.stylized_print('Note added')

        return False
