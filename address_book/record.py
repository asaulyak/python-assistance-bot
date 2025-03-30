from .address import Address
from .birthday import Birthday
from .email import Email
from .name import Name
from .phone import Phone


class Record:
    def __init__(self, name: Name):
        self.name: Name = name
        self.phones: set[Phone] = set()
        self.birthday: Birthday | None = None
        self.address: Address | None = None
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


    def add_address(self, address:Address):
        self.address = address


    def __str__(self):
        birthday = f', Birthday: {str(self.birthday)}' if self.birthday else ''
        phones = f', Phones: {'; '.join(str(p) for p in self.phones)}' if self.phones else ''
        emails = f', Emails: {'; '.join(email.value for email in self.emails)}' if self.emails else ''
        address = f', Address: {self.address.value}' if self.address else ''

        return f"Name: {self.name.value}{birthday}{phones}{emails}{address}"

    def table_data(self):
        name = self.name.value
        emails = '\n'.join(email.value for email in self.emails)
        phones = '\n'.join(str(p) for p in self.phones)
        birthday = str(self.birthday) if self.birthday else ''
        address = self.address.value if self.address else ''


        return (name, emails, phones, birthday, address)