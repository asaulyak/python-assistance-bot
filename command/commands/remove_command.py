from typing import List

from address_book import Record, Name
from command.command import Command
from display import ColorsConstants, StylizedElements
from display.paginator import Paginator
from execution_context import ExecutionContext
from rich.text import Text

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
                StylizedElements.stylized_print('Contact not found', ColorsConstants.ERROR_COLOR.value)

                return False

        else:
            contacts = context.addressbook.to_list()
            paginator = Paginator(contacts)

            index = paginator.show(text='Select a contact to remove')

            if index is None:
                # user interrupted contact removal
                StylizedElements.stylized_print('No records removed', ColorsConstants.ERROR_COLOR.value)

                return  False

            record = contacts[index]

        context.addressbook.delete(record.name)

        message = Text()
        record_text = record.name.value
        message.append('Contact successfully removed: ', ColorsConstants.SUCCESS_COLOR.value)
        message.append(f"Name ", ColorsConstants.INPUT_COLOR.value)
        message.append(record_text, ColorsConstants.HIGHLIGHT_COLOR.value)

        StylizedElements.stylized_print(str(message))

        return False




