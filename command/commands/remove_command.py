from typing import List

from address_book import Record, Name
from command.command import Command
from display import ColorsConstants, StylizedElements
from display.paginator import Paginator
from execution_context import ExecutionContext
from user_input import index_question

class RemoveCommand(Command):
    @property
    def name(self):
        return 'remove'


    @property
    def aliases(self):
        return ['delete', 'rm']


    @property
    def description(self):
        return 'Remove contact from address book'


    def run(self, args: list[str], context: ExecutionContext, commands: List) -> bool:
        record: Record | None = None

        if len(args) >= 1:
            name = args[0]
            record = context.addressbook.find(Name(name))

            if not record:
                StylizedElements.stylized_print('Contact not found', ColorsConstants.ERROR_COLOR._value_)

                return False

        else:
            contacts = list(context.addressbook.values())
            paginator = Paginator(contacts)

            paginator.show()

            index = index_question('Select a contact to remove (or \'q\' to cancel): ', len(context.addressbook) - 1)

            if index is None:
                # user interrupted contact removal
                StylizedElements.stylized_print('No records removed', ColorsConstants.ERROR_COLOR._value_)

                return  False

            record = contacts[index]

        context.addressbook.delete(record.name)

        message = f'Contact successfully removed: {record}'

        StylizedElements.stylized_print(message)

        return False




