from address_book import AddressBook
from notes import Notebook


class ExecutionContext:
    def __init__(self):
        self.addressbook = AddressBook()
        self.notebook = Notebook()