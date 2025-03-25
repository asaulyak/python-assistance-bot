from command.command import Command


class HelpCommand(Command):
    @property
    def name(self):
        return 'help'

    @property
    def aliases(self):
        return ['?']

    def run(self, args, book, commands):
        print('Available commands:')

        for command in commands:
            print(f'  {command.name}', f'({', '.join(alias for alias in command.aliases)})')

        return '', False