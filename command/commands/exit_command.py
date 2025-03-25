from command.command import Command
from execution_context import ExecutionContext
from persistence import save_data


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
        stop = True

        save_data(context)

        return message, stop