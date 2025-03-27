from typing import List

from address_book import Name, Phone
from address_book.birthday import Birthday
from address_book.email import Email
from command.command import Command
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

    def run(self, args: list[str], context: ExecutionContext, commands: List) -> (str, bool):
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
                    return 'Editing canceled', False

                record = list(context.addressbook.values())[index]


        phone = None
        email = None
        birthday = None

        while not phone:
            phone = init_field(Phone, input('Phone:'))

        while not email:
            email = init_field(Email, input('Email:'))

        while not birthday:
            birthday = init_field(Birthday, input('Birthday:'))

        if phone and not phone.is_empty():
            record.add_phone(phone)

        if email and not email.is_empty():
            record.add_email(email)

        if birthday and not birthday.is_empty():
            record.add_birthday(birthday)

        message = f"Contact updated: {record}"

        context.addressbook.add_record(record)

        return message, False


