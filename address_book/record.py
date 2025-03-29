from .birthday import Birthday
from .email import Email
from .name import Name
from .phone import Phone


class Record:
    def __init__(self, name: Name):
        self.name: Name = name
        self.phones: set[Phone] = set()
        self.birthday: Birthday | None = None
        self.emails: set[Email] = set()

    def add_phone(self, phone: Phone):
        self.phones.add(phone)

    def edit_phone(self, phone_number, new_phone):
        new_phone_exists = bool(self.find_phone(new_phone))
        if new_phone_exists:
            raise KeyError(f"Phone number {new_phone} already exists")

        for p in self.phones:
            if p.value == phone_number:
                p.update(new_phone)

                return

        raise ValueError(f"Phone number {phone_number} not found")

    def find_phone(self, phone_number):
        for p in self.phones:
            if p.value == phone_number:

                return p

    def remove_phone(self, phone_number):
        for p in self.phones:
            if p.value == phone_number:
                self.phones.remove(p)

    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def add_email(self, email: Email):
        self.emails.add(email)

    def find_email(self, email):
        for e in self.emails:
            if e.value == email:

                return e


    def __str__(self):
        return f"Name: {self.name.value}, {f'Birthday: {str(self.birthday)},' if self.birthday else '' } Emails: {'; '.join(email.value for email in self.emails)}, Phones: {'; '.join(p.value for p in self.phones)}"

    def table_data(self):
        return (self.name.value, '\n'.join(email.value for email in self.emails), '\n'.join(p.value for p in self.phones), str(self.birthday) if self.birthday else '')