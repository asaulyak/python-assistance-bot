from typing import List

from command.command import Command
from execution_context import ExecutionContext


class BirthdaysCommand(Command):
    @property
    def name(self):
        return 'birthdays'


    @property
    def aliases(self):
        return ['b']


    @property
    def description(self):
        return 'Show upcoming birthdays'


    def run(self, args: list[str], context: ExecutionContext, commands: List) -> (str, bool):
        days_before_birthday = 7

        if len(args) >= 1:
            days = args[0]

            if not days.isnumeric():
                return 'Provide a valid number of days before birthday', False

            days_before_birthday = int(days)

        message = context.book.get_upcoming_birthdays(days_before_birthday)

        return message, False