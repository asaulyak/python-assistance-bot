from typing import List

from address_book import Record, Name
from command.command import Command
from display import ColorsConstants, StylizedElements
from display.paginator import Paginator
from execution_context import ExecutionContext
from user_input import index_question
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
                StylizedElements.stylized_print('Contact not found', ColorsConstants.ERROR_COLOR._value_)

                return False

        else:
            contacts = list(context.addressbook.values())
            paginator = Paginator(contacts)

            index = paginator.show(text='Select a contact to remove')

            if index is None:
                # user interrupted contact removal
                StylizedElements.stylized_print('No records removed', ColorsConstants.ERROR_COLOR._value_)

                return  False

            record = contacts[index]

        context.addressbook.delete(record.name)

        message = Text()
        record_text = str(record).split(' ')
        message.append('Contact successfully removed: ', ColorsConstants.SUCCESS_COLOR.value)
        message.append(f"{record_text[0]} ", ColorsConstants.INPUT_COLOR.value)
        message.append(record_text[1], ColorsConstants.HIGHLIGHT_COLOR.value)

        StylizedElements.stylized_print(message)

        return False




