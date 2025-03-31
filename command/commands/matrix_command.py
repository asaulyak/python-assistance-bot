from command.command import Command
from display import matrix_rain

class MatrixCommand(Command):

    @property
    def name(self):
        return 'matrix'


    @property
    def aliases(self):
        return ['m', 'rain']


    @property
    def description(self):
        return 'Show matrix rain'
    def run(self, args, context, commands):
        
        delay = 5 if not len(args) else int(args[0])
        matrix_rain(delay)