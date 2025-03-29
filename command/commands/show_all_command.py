from typing import List

from command.command import Command
from execution_context import ExecutionContext
from display import StylizedElements,ColorsConstants,TableBuilder


class ShowAllCommand(Command):
    @property
    def name(self):
        return 'all'

    @property
    def aliases(self):
        return ['showall']

    @property
    def description(self):
        return 'Show all contacts from the address book'


    def run(self, args: list[str], context: ExecutionContext, commands: List) -> (str, bool):

        if context.addressbook.is_empty():
            StylizedElements.stylized_input('Address book is empty',ColorsConstants.WARNING_COLOR.value)
            return '', False
        
        table_title = 'Address book'
        table_headers = ('name', 'emails','phones','birthday')
        table_data = context.addressbook.table_data()
    


        table = TableBuilder()
        table.set_title(table_title)
        table.set_table_headers(table_headers)
        table.set_table_data(table_data)
        table.show()

        return '', False