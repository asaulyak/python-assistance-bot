from command.command import Command
from execution_context import ExecutionContext
from persistence import save_data


class SaveCommand(Command):
    @property
    def name(self):
        return 'save'


    @property
    def aliases(self):
        return ['s']


    @property
    def description(self):
        return 'Saves current state to the storage'



    def run(self, _, context: ExecutionContext, *args):
        message = 'Data successfully saved'
        stop = False

        save_data(context)

        return message, stop