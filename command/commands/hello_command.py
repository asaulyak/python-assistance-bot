from command.command import Command


class HelloCommand(Command):
    @property
    def name(self):
        return 'hello'


    @property
    def aliases(self):
        return ['hi', 'start', 'begin']
    
    @property
    def description(self):
        return 'Greet the user'


    @property
    def description(self):
        return 'Say hello to the user'


    def run(self, *args):
        message = "How can I help you?"
        stop = False

        return message, stop