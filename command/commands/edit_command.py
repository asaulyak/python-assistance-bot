from typing import List

from address_book import Name, Phone, Address
from address_book.birthday import Birthday
from address_book.email import Email
from command.command import Command
from display import StylizedElements, ColorsConstants
from display.paginator import Paginator
from execution_context import ExecutionContext
from field import init_field
from user_input import index_question


class EditCommand(Command):

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
        args_len = len(args)

        name = args[0] if args_len >= 1 else None

        record = context.addressbook.find(Name(name)) if name else None

        if name and not record:
            print('Name not found in the address book')

        if not record:
            print('Pick an existing contact to edit')

            paginator = Paginator(list(context.addressbook.values()))
            paginator.show(True)

            while not record:
                index = index_question('Type an index of a contact to edit (or \'q\' to cancel): ', len(context.addressbook))

                if index is None:
                    StylizedElements.stylized_print('Editing canceled', ColorsConstants.ERROR_COLOR.value)
                    return False

                record = list(context.addressbook.values())[index]


        phone = None
        email = None
        birthday = None
        address= None

        while not phone:
            phone = init_field(Phone, input('Phone: '))

        while not email:
            email = init_field(Email, input('Email: '))

        while not birthday:
            birthday = init_field(Birthday, input('Birthday: '))

        while not address:
            address = init_field(Address, input('Address: '))

        if phone and not phone.is_empty():
            record.add_phone(phone)

        if email and not email.is_empty():
            record.add_email(email)

        if birthday and not birthday.is_empty():
            record.add_birthday(birthday)

        if address and not address.is_empty():
            record.add_address(address)

        context.addressbook.add_record(record)

        StylizedElements.stylized_print(f"Contact updated: {record}", ColorsConstants.SUCCESS_COLOR.value)

        return False


