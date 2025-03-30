from typing import List

from address_book import Record, Name, Phone, AddressBook, Address
from address_book.birthday import Birthday
from address_book.email import Email
from command.command import Command
from execution_context import ExecutionContext
from field import init_field
from user_input import yes_no_question
from display import StylizedElements, ColorsConstants
from rich.text import Text
from display.text_animation import MatrixTextLoader


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

    def run(self, args: list[str], context: ExecutionContext, commands: List) -> bool:
        args_len = len(args)

        # get contact details from args if provided by a user
        name = None if args_len < 1 else init_field(Name, args[0])
        phone = None if args_len < 2 else init_field(Phone, args[1])
        email = None if args_len < 3 else init_field(Email, args[2])
        birthday = None if args_len < 4 else init_field(Birthday, args[3])
        address = None

        name = self.__check_name_existence(context.addressbook, name) if name else None
        

        while not name or name.is_empty():
            name = init_field(Name, StylizedElements.stylized_input(MatrixTextLoader('Name: '), ColorsConstants.INPUT_COLOR.value))
            name = self.__check_name_existence(context.addressbook, name) if name else None

        while not phone:
            phone = init_field(Phone, StylizedElements.stylized_input('Phone: ', ColorsConstants.INPUT_COLOR.value))

        while not email:
            email = init_field(Email, StylizedElements.stylized_input('Email: ', ColorsConstants.INPUT_COLOR.value))

        while not birthday:
            birthday = init_field(Birthday, StylizedElements.stylized_input('Birthday: ', ColorsConstants.INPUT_COLOR.value))

        while not address:
            address = init_field(Address, StylizedElements.stylized_input('Address: ', ColorsConstants.INPUT_COLOR.value))


        # get an existing record or create one with the provided name
        record = context.addressbook.find(name, Record(name))

        if phone and not phone.is_empty():
            record.add_phone(phone)

        if email and not email.is_empty():
            record.add_email(email)

        if birthday and not birthday.is_empty():
            record.add_birthday(birthday)

        if address and not address.is_empty():
            record.add_address(address)

       
        is_present = context.addressbook.find(name)
        message = Text()
        record_text = record.name.value
        message.append(f"Contact successfully {"updated" if is_present else "added"}: ", ColorsConstants.SUCCESS_COLOR.value)
        message.append("Name ", ColorsConstants.INPUT_COLOR.value)
        message.append(record_text, ColorsConstants.HIGHLIGHT_COLOR.value)

        StylizedElements.stylized_print(message)


        context.addressbook.add_record(record)

        return False


    def __check_name_existence(self, book: AddressBook, name: Name) -> Name | None:
        existing_record = book.find(name)

        if existing_record:
            StylizedElements.stylized_print('Name already exists in the address book. Provide a new one', ColorsConstants.ERROR_COLOR.value)
            return None

        return name