from typing import List,Tuple

from address_book import Name, Phone, Record
from address_book.email import Email
from command.command import Command
from execution_context import ExecutionContext
from display import StylizedElements,ColorsConstants,TableBuilder


class FindCommand(Command):
    def __init__(self):
        self.__find_options = ['Name', 'Phone', 'Email', 'Query']

    @property
    def name(self):
        return 'find'


    @property
    def aliases(self):
        return ['f', 'search']

    @property
    def description(self):
        return 'Find contact by name, phone, email or query'

    def run(self, args: list[str], context: ExecutionContext, commands: List) -> bool:
        
        name: Name | None = None
        phone: Phone | None = None
        email: Email | None = None
        query: str | None = None

        records: list[Record] = []

        term = args[0] if len(args) >= 1 else None

        if term:
            possible_phone, possible_email, possible_name, possible_query = self.__guess_find_option(term)

            if possible_phone:
                phone = possible_phone
            elif possible_email:
                email = possible_email
            elif possible_name:
                name = possible_name
            elif possible_query:
                query = possible_query 
        else:
            # console menu
            user_answer = StylizedElements.console_menu('Select a field to search for', self.__find_options)
            index = self.__find_options.index(user_answer)

            while True:
                class_name = self.__find_options[index]

                term = StylizedElements.stylized_input(f'Provide {class_name}: ', ColorsConstants.INPUT_COLOR.value)

                try:
                    if class_name == 'Query':
                        query = term
                    else:
                        parsed = globals()[class_name](term)

                        if index == 0:
                            name = parsed
                        elif index == 1:
                            phone = parsed
                        elif index == 2:
                            email = parsed
                    break
                except:
                    StylizedElements.stylized_print(f'Invalid {class_name}', ColorsConstants.ERROR_COLOR.value)
                    

        if name:
            records = context.addressbook.find_by_name(name)
        elif phone:
            records = context.addressbook.find_by_phone(phone)
        elif email:
            records = context.addressbook.find_by_email(email)
        elif query:
            records = context.addressbook.find_by_query(query)


        if len(records) == 0:
            StylizedElements.stylized_print('Nothing found', ColorsConstants.WARNING_COLOR.value)
       
        if len(records) > 0:
            table_title = 'Address book'
            table_headers = ('name', 'emails','phones','birthday', 'address')
            table_data = [record.table_data() for record in records]            

            table = TableBuilder()
            table.set_title(table_title)
            table.set_table_headers(table_headers)
            table.set_table_data(table_data)
            table.set_highlight_text(term)
            table.show()
            

        return False


    def __show_find_options(self):
        for i, option in enumerate(self.__find_options):
            print(f'[{i}] {option}')


    def __guess_find_option(self, value: str) -> Tuple | None:
        name: Name | None = None
        phone: Phone | None = None
        email: Email | None = None
        query: str | None = None

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

        if not name and not phone and not email:
            query = value



        return phone, email, name, query