from command.command import Command
from execution_context import ExecutionContext
from persistence import save_data
from display import StylizedElements


class ExitCommand(Command):
    @property
    def name(self):
        return 'exit'


    @property
    def aliases(self):
        return ['close']


    @property
    def description(self):
        return 'Exit the assistance bot and save current file'



    def run(self, _, context: ExecutionContext, *args):
        message = 'Good bye!'
        StylizedElements.fancy_text(message)

        save_data(context)

        return True