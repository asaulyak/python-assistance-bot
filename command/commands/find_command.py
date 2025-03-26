from typing import List, Tuple

from address_book import Name, Phone, Record
from address_book.email import Email
from command.command import Command
from execution_context import ExecutionContext
from user_input.user_input import index_question


class FindCommand(Command):
    def __init__(self):
        self.__find_options = ['Name', 'Phone', 'Email']

    @property
    def name(self):
        return 'find'


    @property
    def aliases(self):
        return ['f', 'search']

    @property
    def description(self):
        return 'Find contact by name, phone or email'

    def run(self, args: list[str], context: ExecutionContext, commands: List) -> (str, bool):
        name: Name | None = None
        phone: Phone | None = None
        email: Email | None = None

        records: list[Record] = []

        term = args[0] if len(args) >= 1 else None

        if term:
            possible_phone, possible_email, possible_name = self.__guess_find_option(term)

            if possible_phone:
                phone = possible_phone
            elif possible_email:
                email = possible_email
            elif possible_name:
                name = possible_name
        else:
            print('Select a field to search for')

            self.__show_find_options()

            index = index_question('Type an index of the field: ', 2)

            while True:
                class_name = self.__find_options[index]

                term = input(f'Provide {class_name}: ')

                try:
                    parsed = globals()[class_name](term)

                    if index == 0:
                        name = parsed
                    elif index == 1:
                        phone = parsed
                    elif index == 2:
                        email = parsed

                    break
                except:
                    print(f'Invalid {class_name}')

        if name:
            found = context.book.find(name)

            if found:
                records.append(found)
        elif phone:
            records = context.book.find_by_phone(phone)
        elif email:
            records = context.book.find_by_email(email)

        message = 'Nothing found'

        if len(records) > 0:
            message = '\n'.join([str(record) for record in records])

        return message, False


    def __show_find_options(self):
        for i, option in enumerate(self.__find_options):
            print(f'[{i}] {option}')


    def __guess_find_option(self, value: str) -> Tuple | None:
        name: Name | None = None
        phone: Phone | None = None
        email: Email | None = None

        try:
            phone = Phone(value)
        except:
            pass

        try:
            email = Email(value)
        except:
            pass

        try:
            name = Name(value)
        except:
            pass


        return phone, email, name