from collections import UserDict
from .note import Note

class NoteBook(UserDict):
    def add_note(self, note: Note):
        self.data[note.title.value] = note
    
    def all_notes(self):
        return self.data.values()
    
    def __str__(self):
        return f'Notes Book: \n {'\n '.join(str(note) for note in self.data.values())}'