from typing import List

from command.command import Command
from execution_context import ExecutionContext


class NoteShowAllCommand(Command):
    @property
    def name(self):
        return 'all-notes'

    @property
    def description(self):
        return 'Show all notes'


    def run(self, args: list[str], context: ExecutionContext, commands: List) -> (str, bool):
        message = str(context.notebook)

        return message, False