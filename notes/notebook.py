from collections import UserList
from notes import Note, Tag


class Notebook(UserList):
    def add(self, note: Note):
        self.data.append(note)


    def find(self, term: str) -> list[Note]:
        return [note for note in self.data if term in note.title.value]


    def find_by_tag(self, tag: Tag):
        return [note for note in self.data if any(note_tag for note_tag in note.tags if note_tag.value == tag.value)]


    def delete(self, note: Note):
        return self.data.remove(note)


    def is_empty(self):
        return len(self.data) == 0


    def __str__(self):
        if self.is_empty():
            return 'Notebook is empty'

        return f'NoteBook:\n {'\n '.join(str(note) for note in self.data)}'