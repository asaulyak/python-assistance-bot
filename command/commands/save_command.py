from command.command import Command
from display import StylizedElements
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
        return 'Save current state to the storage'



    def run(self, _, context: ExecutionContext, *args) -> bool:
        message = 'Data successfully saved'
        stop = False

        save_data(context)

        StylizedElements.stylized_print(message)

        return stop