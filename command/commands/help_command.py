from command.command import Command
from display import TableBuilder


class HelpCommand(Command):
    @property
    def name(self):
        return 'help'

    @property
    def aliases(self):
        return ['?']
    
    @property
    def description(self):
        return 'Show available commands'

    def run(self, args, book, commands):        
        table_title = 'Available commands'
        table_headers = ('command', 'description')
        table_data = [(command.name, command.description) for command in commands]

        TableBuilder(table_title,table_headers,table_data)
        

        return '', False