from address_book import AddressBook
from note_book import NoteBook, Note


class ExecutionContext:
    def __init__(self):
        self.book = AddressBook()
        self.note: list[Note] = NoteBook()