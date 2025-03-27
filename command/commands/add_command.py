from typing import List

from address_book import Record, Name, Phone, AddressBook
from address_book.birthday import Birthday
from address_book.email import Email
from command.command import Command
from execution_context import ExecutionContext
from field import init_field
from user_input import yes_no_question


class AddCommand(Command):
    @property
    def name(self):
        return 'add'


    @property
    def aliases(self):
        return ['a', 'create']


    @property
    def description(self):
        return 'Add new record to address book'

    def run(self, args: list[str], context: ExecutionContext, commands: List) -> (str, bool):
        args_len = len(args)

        # get contact details from args if provided by a user
        name = None if args_len < 1 else init_field(Name, args[0])
        phone = None if args_len < 2 else init_field(Phone, args[1])
        email = None if args_len < 3 else init_field(Email, args[2])
        birthday = None if args_len < 4 else init_field(Birthday, args[3])

        # reset the name to None if user doesn't want to edit existing record
        name = self.__check_name_existence(context.addressbook, name) if name else None

        while not name or name.is_empty():
            name = init_field(Name, input('Name: '))
            name = self.__check_name_existence(context.addressbook, name) if name else None

        while not phone:
            phone = init_field(Phone, input('Phone: '))

        while not email:
            email = init_field(Email, input('Email: '))

        while not birthday:
            birthday = init_field(Birthday, input('Birthday: '))

        # get an existing record or create one with the provided name
        record = context.addressbook.find(name, Record(name))

        if phone and not phone.is_empty():
            record.add_phone(phone)

        if email and not email.is_empty():
            record.add_email(email)

        if birthday and not birthday.is_empty():
            record.add_birthday(birthday)

        message = f"Contact added: {record}"

        context.addressbook.add_record(record)

        return message, False


    def __check_name_existence(self, book: AddressBook, name: Name) -> Name | None:
        existing_record = book.find(name)

        if existing_record:
            should_edit = yes_no_question('Name already exists in the address book. Do you want to edit the record?')

            if should_edit:
                print('OK. Let\'s update the record')

                return name
            else:
                return None

        return name