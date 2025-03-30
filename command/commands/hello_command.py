from command.command import Command
from display import StylizedElements,ColorsConstants


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
        StylizedElements.stylized_print("How can I help you?",ColorsConstants.INPUT_COLOR.value)
        stop = False

        return stop