from collections import UserList
from .note import Note

class NoteBook(UserList):
    def add_note(self, note: Note):
        self.data.append(note)
    
    def all_notes(self):
        return self.data.values() 
    
    def delete():
        ...

    def find(self, title, default = None) -> Note:
        #Find - via keyword search in title or in the body
        return self.data.get(title.value, default)

    def update():
        ...
    
    def __str__(self):
        return f'Notes Book: \n {'\n '.join(str(note) for note in self.data.values())}'