from command.command import Command
from display import TableBuilder



class HelpCommand(Command):
    @property
    def name(self):
        return 'help'

    @property
    def aliases(self):
        return ['?', 'h', 'menu']

    @property
    def description(self):
        return 'Show available commands'

    def run(self, args, context, commands):
        sorted_commands = sorted(commands, key=lambda command: (command.name.endswith('note') or command.name.endswith('notes'), command.name))

        table_title = 'Available commands'
        table_headers = ('command', 'description',)
        table_data = [(f"{command.name:<12} [ {', '.join(command.aliases)} ]", command.description) for command in sorted_commands]


        table = TableBuilder()
        table.set_title(table_title)
        table.set_table_headers(table_headers)
        table.set_table_data(table_data)
        table.show()
        

        return False