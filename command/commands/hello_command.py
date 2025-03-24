from command.command import Command


class HelloCommand(Command):
    @property
    def name(self):
        return 'hello'


    @property
    def aliases(self):
        return ['hi', 'start', 'begin']


    def run(self, *args):
        message = "How can I help you?"
        stop = False

        return message, stop