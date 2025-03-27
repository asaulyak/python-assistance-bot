from typing import List

from address_book import Record, Name
from command.command import Command
from display.paginator import Paginator
from execution_context import ExecutionContext
from user_input.user_input import index_question


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


    def run(self, args: list[str], context: ExecutionContext, commands: List) -> (str, bool):
        record: Record | None = None

        if len(args) >= 1:
            name = args[0]
            record = context.book.find(Name(name))

            if not record:
                return 'Contact not found', False

        else:
            contacts = list(context.book.values())
            paginator = Paginator(contacts)

            paginator.show()

            index = index_question('Select a contact to remove: ', len(context.book) - 1)

            record = contacts[index]

        context.book.delete(record.name)

        message = f'Contact successfully removed: {record}'

        return message, False




