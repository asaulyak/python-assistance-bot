from typing import List

from command.command import Command
from execution_context import ExecutionContext
from notes import Title, Tag, Note
from user_input import index_question


class NoteFineCommand(Command):
    @property
    def name(self):
        return 'find-note'

    @property
    def aliases(self):
        return ['fn']


    @property
    def description(self):
        return 'Find a note by title or tag'


    def run(self, _, context: ExecutionContext, __) -> Tup(str, bool):
        options = [Title.__name__, Tag.__name__]

        for i, option in enumerate(options):
            print(f'[{i}] {option}')


        index = index_question('Select field to search: ', len(options) - 1)

        if index is None:
            return 'Exiting..', False

        field_name = options[index]

        term = input(f'Type {field_name}: ')

        notes: list[Note] = []

        if index == 0:
            notes = context.notebook.find(term)
        elif index == 1:
            notes = context.notebook.find_by_tag(term)

        message = 'Nothing found'

        if len(notes) > 0:
            message = '\n'.join([str(note) for note in notes])

        return message, False