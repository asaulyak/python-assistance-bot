from command.command import Command


class HelpCommand(Command):
    @property
    def name(self):
        return 'help'

    @property
    def aliases(self):
        return ['?']

    @property
    def description(self):
        return 'Shows available commands'

    def run(self, _, __, commands):
        print('Available commands:')

        for command in commands:
            print(f'  {command.name}',
                  f'[{', '.join(alias for alias in command.aliases)}]' if len(command.aliases) else '',
                  f'- {command.description}')

        return '', False