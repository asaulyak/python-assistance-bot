from typing import List,Tuple

from command.command import Command
from execution_context import ExecutionContext
from display import StylizedElements,ColorsConstants,TableBuilder


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
                StylizedElements.stylized_print('Provide a valid number of days before birthday', ColorsConstants.ERROR_COLOR.value)
                return '', False

            days_before_birthday = int(days)
        
        table_title = 'Upcoming birthdays'
        table_headers = ('date','day', 'name',)
        table_data = context.addressbook.get_upcoming_birthdays(days_before_birthday)
        if len(table_data) == 0:
            return '', False
        
        table = TableBuilder()
        table.set_title(table_title)
        table.set_table_headers(table_headers)
        table.set_table_data(table_data)
        table.show()


        return '', False