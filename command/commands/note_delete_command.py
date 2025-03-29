from typing import List

from command.command import Command
from display import StylizedElements
from display.paginator import Paginator
from execution_context import ExecutionContext
from user_input import index_question


class NoteDeleteCommand(Command):
    @property
    def name(self):
        return 'delete-note'


    @property
    def aliases(self):
        return ['dn']


    @property
    def description(self):
        return 'Delete note'


    def run(self, args: list[str], context: ExecutionContext, commands: List) -> bool:
        paginator = Paginator(context.notebook)
        paginator.show()

        index = index_question('Type index of a note (or \'q\' to cancel): ', len(context.notebook) - 1)

        if index is None:
            StylizedElements.stylized_print('No notes were deleted')
            return False

        note = context.notebook[index]
        context.notebook.delete(note)

        StylizedElements.stylized_print('Note deleted')

        return False