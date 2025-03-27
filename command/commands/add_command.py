from typing import List

from address_book import Record, Name, Phone, AddressBook
from address_book.birthday import Birthday
from address_book.email import Email
from address_book.empty_field import EmptyField
from command.command import Command
from execution_context import ExecutionContext
from field import Field
from user_input.user_input import yes_no_question


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
        name = None if args_len < 1 else self.__init_field(Name, args[0])
        phone = None if args_len < 2 else self.__init_field(Phone, args[1])
        email = None if args_len < 3 else self.__init_field(Email, args[2])
        birthday = None if args_len < 4 else self.__init_field(Birthday, args[3])

        # reset the name to None if user doesn't want to edit existing record
        name = self.__check_name_existence(context.book, name) if name else None

        while not name or name.is_empty():
            name = self.__init_field(Name, input('Name: '))
            name = self.__check_name_existence(context.book, name) if name else None

        while not phone:
            phone = self.__init_field(Phone, input('Phone: '))

        while not email:
            email = self.__init_field(Email, input('Email: '))

        while not birthday:
            birthday = self.__init_field(Birthday, input('Birthday: '))

        # get an existing record or create one with the provided name
        record = context.book.find(name, Record(name))

        if phone and not phone.is_empty():
            record.add_phone(phone)

        if email and not email.is_empty():
            record.add_email(email)

        if birthday and not birthday.is_empty():
            record.add_birthday(birthday)

        message = f"Contact added: {record}"

        context.book.add_record(record)

        return message, False


    def __init_field(self, constructor: type(Field), value: str | None) -> Field | None:
        if value == '':
            return EmptyField(value)

        if not value:
            return None

        try:
            return constructor(value)
        except Exception as e:
            print(str(e))

            return None

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