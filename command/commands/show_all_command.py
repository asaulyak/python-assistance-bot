from typing import List

from command.command import Command
from execution_context import ExecutionContext


class ShowAllCommand(Command):
    @property
    def name(self):
        return 'all'

    @property
    def aliases(self):
        return ['showall']

    @property
    def description(self):
        return 'Shows all contacts from teh address book'


    def run(self, args: list[str], context: ExecutionContext, commands: List) -> [str, bool]:
        message = str(context.book)

        return message, False