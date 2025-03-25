from address_book import AddressBook
from typing import List


class Command:
    def __init__(self):
        pass


    @property
    def name(self):
        return 'empty'


    @property
    def aliases(self):
        return []


    @property
    def description(self):
        return 'default description'


    def run(self, args, book: AddressBook, commands: List):
        pass
