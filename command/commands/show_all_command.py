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
        return 'Show all contacts from the address book'


    def run(self, args: list[str], context: ExecutionContext, commands: List) -> (str, bool):
        message = str(context.book)

        return message, False