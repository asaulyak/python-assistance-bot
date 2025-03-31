import time
from command.command import Command
from execution_context import ExecutionContext
from persistence import save_data
from display import StylizedElements,matrix_rain



class ExitCommand(Command):
    @property
    def name(self):
        return 'exit'


    @property
    def aliases(self):
        return ['close', "quit"]


    @property
    def description(self):
        return 'Exit the assistance bot and save current file'



    def run(self, _, context: ExecutionContext, *args):
        message = 'Good bye!'
        StylizedElements.fancy_text(message)
        time.sleep(2)
        matrix_rain(20)

        save_data(context)

        return True