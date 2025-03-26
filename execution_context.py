from address_book import AddressBook
from notes.note import Note


class ExecutionContext:
    def __init__(self):
        self.book = AddressBook()
        self.notes: list[Note] = []