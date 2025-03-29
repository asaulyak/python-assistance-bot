from command.command import Command
from display import StylizedElements


class HelloCommand(Command):
    @property
    def name(self):
        return 'hello'


    @property
    def aliases(self):
        return ['hi', 'start']


    @property
    def description(self):
        return 'Say hello to the user'


    def run(self, *args):
        StylizedElements.stylized_print("How can I help you?")
        stop = False

        return stop