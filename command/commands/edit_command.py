from typing import List

from address_book import Name, Field, Phone, AddressBook
from address_book.birthday import Birthday
from address_book.email import Email
from address_book.empty_field import EmptyField
from command.command import Command
from execution_context import ExecutionContext
from user_input.user_input import yes_no_question, index_question


class EditCommand(Command):
    def __init__(self):
        self.__records_cursor = 0

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

        record = context.book.find(Name(name)) if name else None

        if name and not record:
            print('Name not found in the address book')

        if not record:
            print('Pick an existing contact to edit')

            self.__show_available_contacts(context.book, True)

            items_to_show_exist = len(context.book) > self.__records_cursor

            while items_to_show_exist:
                show_more = yes_no_question('Show more?')

                if not show_more:
                    break

                self.__show_available_contacts(context.book, False)
                items_to_show_exist = len(context.book) > self.__records_cursor

            while not record:
                index = index_question('Type an index of a contact to edit: ', len(context.book))

                record = list(context.book.values())[index]


        phone = None
        email = None
        birthday = None

        while not phone:
            phone = self.__init_field(Phone, input('Phone:'))

        while not email:
            email = self.__init_field(Email, input('Email:'))

        while not birthday:
            birthday = self.__init_field(Birthday, input('Birthday:'))

        if phone and not phone.is_empty():
            record.add_phone(phone)

        if email and not email.is_empty():
            record.add_email(email)

        if birthday and not birthday.is_empty():
            record.add_birthday(birthday)

        message = f"Contact updated: {record}"

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


    def __show_available_contacts(self, book: AddressBook, reset_cursor = False, max_records = 10):
        if reset_cursor:
            self.__records_cursor = 0

        start = self.__records_cursor
        end = start + max_records

        for i, (key,record) in enumerate(list(book.items())[start:end]):
            print(f'[{i + start}] {record}')


        self.__records_cursor = end