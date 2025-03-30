import re

from typing import List

from address_book import Name, Phone, Address
from address_book.birthday import Birthday
from address_book.email import Email
from command.command import Command
from display import StylizedElements, ColorsConstants
from display.paginator import Paginator
from execution_context import ExecutionContext
from field import init_field
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from rich.text import Text


class EditCommand(Command):
    '''
    Edit a record in the address book.
    '''

    @property
    def name(self):
        return 'edit'


    @property
    def aliases(self):
        return ['e', 'change']


    @property
    def description(self):
        return 'Update a record in the address book'

    def run(self, args: list[str], context: ExecutionContext, commands: List) -> bool:
        
        if len(context.addressbook.items()) == 0:
            StylizedElements.stylized_print('Address book is empty', ColorsConstants.WARNING_COLOR.value)
            return False

        args_len = len(args)

        name = args[0] if args_len >= 1 else None

        record = context.addressbook.find(Name(name)) if name else None

        if name and not record:
            StylizedElements.stylized_print('Name not found in the address book', ColorsConstants.WARNING_COLOR.value)

        if not record:

            paginator = Paginator(list(context.addressbook.values()))

            index = paginator.show(text='Pick an existing contact to edit') 

            if index is None:
                StylizedElements.stylized_print('Editing canceled', ColorsConstants.ERROR_COLOR.value)
                return False

            record = list(context.addressbook.values())[index]


        phone = None
        email = None
        birthday = None
        address= None

        print(str(record))

        style = Style.from_dict({
            'prompt': ColorsConstants.INPUT_COLOR.value,
        })
        while not phone:
            new_phone = prompt('Phone: ', default=" ".join(re.sub(r"\D", "",str(p)) for p in record.phones), style=style)
            phone = init_field(Phone, new_phone)

        while not email:
            new_email = prompt('Email: ', default=" ".join(email.value for email in record.emails), style=style)
            email = init_field(Email, new_email)

        while not birthday:
            new_birthday = prompt('Birthday: ', default= str(record.birthday) if record.birthday else '', style=style)
            birthday = init_field(Birthday, new_birthday)

        while not address:
            new_address = prompt('Address: ', default= str(record.address) if record.address else '', style=style)
            address = init_field(Address, new_address)

        if phone and not phone.is_empty():
            record.add_phone(phone)

        if email and not email.is_empty():
            record.add_email(email)

        if birthday and not birthday.is_empty():
            record.add_birthday(birthday)

        if address and not address.is_empty():
            record.add_address(address)

        context.addressbook.add_record(record)

        message = Text()
        record_text = record.name.value
        message.append(f"Contact updated: ", ColorsConstants.SUCCESS_COLOR.value)
        message.append(f"Name ", ColorsConstants.INPUT_COLOR.value)
        message.append(record_text, ColorsConstants.HIGHLIGHT_COLOR.value)

        StylizedElements.stylized_print(f"Contact updated: {record}", ColorsConstants.SUCCESS_COLOR.value)

        return False


