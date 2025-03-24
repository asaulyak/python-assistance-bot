from command.command import Command


class DefaultCommand (Command):
    @property
    def name(self):
        return 'default'


    def run(self):
        message = "Invalid command."
        stop = False

        return message, stop

