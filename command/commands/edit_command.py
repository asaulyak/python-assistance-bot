import re

from typing import List

from address_book import Name, Phone, Address, Record, AddressBook
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

        options_paginator = Paginator(['Name', 'Phones', 'Emails', 'Birthday', 'Address'])

        field_index = options_paginator.show('Select a field to update')

        match field_index:
            case 0:
                self.__edit_name(record, context.addressbook)
            case 1:
                self.__edit_phones(record)
            case 2:
                self.__edit_emails(record)

        # while True:
        #
        #     options_index = options_paginator.show(text='Select what needs to be edited')
        #
        #     self.__edit_phones(record)
        #
        #     if options_index is None:
        #         break
        #
        # print('options_index', options_index)
        #
        # style = Style.from_dict({
        #     'prompt': ColorsConstants.INPUT_COLOR.value,
        # })
        # while not phone:
        #     new_phone = prompt('Phone: ', default=" ".join(re.sub(r"\D", "",str(p)) for p in record.phones), style=style)
        #     phone = init_field(Phone, new_phone)
        #
        # while not email:
        #     new_email = prompt('Email: ', default=" ".join(email.value for email in record.emails), style=style)
        #     email = init_field(Email, new_email)
        #
        # while not birthday:
        #     new_birthday = prompt('Birthday: ', default= str(record.birthday) if record.birthday else '', style=style)
        #     birthday = init_field(Birthday, new_birthday)
        #
        # while not address:
        #     new_address = prompt('Address: ', default= str(record.address) if record.address else '', style=style)
        #     address = init_field(Address, new_address)
        #
        # if phone and not phone.is_empty():
        #     record.add_phone(phone)
        #
        # if email and not email.is_empty():
        #     record.add_email(email)
        #
        # if birthday and not birthday.is_empty():
        #     record.add_birthday(birthday)
        #
        # if address and not address.is_empty():
        #     record.add_address(address)

        context.addressbook.add_record(record)

        message = Text()
        record_text = record.name.value
        message.append(f"Contact updated: ", ColorsConstants.SUCCESS_COLOR.value)
        message.append(f"Name ", ColorsConstants.INPUT_COLOR.value)
        message.append(record_text, ColorsConstants.HIGHLIGHT_COLOR.value)

        StylizedElements.stylized_print(f"Contact updated: {record}", ColorsConstants.SUCCESS_COLOR.value)

        return False



    def __edit_phones(self, record: Record):
        action_options = ['Add', 'Remove', 'Update']
        actions_paginator = Paginator(action_options)
        style = Style.from_dict({
            'prompt': ColorsConstants.INPUT_COLOR.value,
        })

        while True:
            action_index = actions_paginator.show('Select action')

            if action_index is None:
                break

            match action_index:
                case 0:
                    while True:
                        new_phone = prompt('Phone: ', style=style)
                        phone = init_field(Phone, new_phone)

                        if phone and not phone.is_empty():
                            record.add_phone(phone)
                            StylizedElements.stylized_print(f'Phone added {str(phone)}', ColorsConstants.SUCCESS_COLOR.value)

                            break
                case 1:
                    phones_options = [str(phone) for phone in record.phones]
                    remove_paginator = Paginator(phones_options)
                    remove_phone_index = remove_paginator.show('Select a phone to remove')

                    if remove_phone_index is None:
                        break

                    phone_to_remove = next((phone for phone in record.phones if str(phone) == phones_options[remove_phone_index]), None)

                    if phone_to_remove is not None:
                        record.remove_phone(phone_to_remove)
                        StylizedElements.stylized_print(f'Phone removed {str(phone_to_remove)}',
                                                        ColorsConstants.SUCCESS_COLOR.value)

                case 2:
                    phones_options = [str(phone) for phone in record.phones]
                    update_paginator = Paginator(phones_options)
                    update_phone_index = update_paginator.show('Select a phone to update')

                    if update_paginator is None:
                        break

                    phone_to_update = next(
                        (phone for phone in record.phones if str(phone) == phones_options[update_phone_index]), None)


                    while True:
                        new_phone_input = prompt('Phone: ', default=phone_to_update.value, style=style)
                        new_phone = init_field(Phone, new_phone_input)

                        if new_phone and not new_phone.is_empty():
                            StylizedElements.stylized_print(f'Phone updated {str(phone_to_update)} => {str(new_phone)}', ColorsConstants.SUCCESS_COLOR.value)
                            record.edit_phone(phone_to_update, new_phone)

                            break


    def __edit_emails(self, record: Record):
        action_options = ['Add', 'Remove', 'Update']
        actions_paginator = Paginator(action_options)
        style = Style.from_dict({
            'prompt': ColorsConstants.INPUT_COLOR.value,
        })

        while True:
            action_index = actions_paginator.show('Select action')

            if action_index is None:
                break

            match action_index:
                case 0:
                    while True:
                        new_email = prompt('Email: ', style=style)
                        email = init_field(Email, new_email)

                        if email and not email.is_empty():
                            record.add_email(email)
                            StylizedElements.stylized_print(f'Email added {str(email)}', ColorsConstants.SUCCESS_COLOR.value)

                            break
                case 1:
                    email_options = [str(email) for email in record.emails]
                    remove_paginator = Paginator(email_options)
                    remove_email_index = remove_paginator.show('Select an email to remove')

                    if remove_email_index is None:
                        break

                    email_to_remove = next((email for email in record.emails if str(email) == email_options[remove_email_index]), None)

                    if email_to_remove is not None:
                        record.remove_email(email_to_remove)
                        StylizedElements.stylized_print(f'Email removed {str(email_to_remove)}',
                                                        ColorsConstants.SUCCESS_COLOR.value)

                case 2:
                    email_options = [str(email) for email in record.emails]
                    update_paginator = Paginator(email_options)
                    update_email_index = update_paginator.show('Select an email to update')

                    if update_paginator is None:
                        break

                    email_to_update = next(
                        (email for email in record.emails if str(email) == email_options[update_email_index]), None)


                    while True:
                        new_email_input = prompt('Email: ', default=email_to_update.value, style=style)
                        new_email = init_field(Email, new_email_input)

                        if new_email and not new_email.is_empty():
                            StylizedElements.stylized_print(f'Email updated {str(email_to_update)} => {str(new_email)}', ColorsConstants.SUCCESS_COLOR.value)
                            record.edit_email(email_to_update, new_email)

                            break


    def __edit_name(self, record: Record, book: AddressBook):
        while True:
            input_name = StylizedElements.stylized_input('Type name: ', ColorsConstants.INPUT_COLOR.value)
            name = init_field(Name, input_name)

            if name and not name.is_empty():
                if book.find(name):
                    StylizedElements.stylized_print('Contact with such name already exists, choose another one', ColorsConstants.WARNING_COLOR.value)
                    continue

                book.delete(record.name)
                record.set_name(name)
                book.add_record(record
                                )
                StylizedElements.stylized_print('Name updated', ColorsConstants.SUCCESS_COLOR.value)
                break