"""
This module defines the Notebook class, a container for managing a collection of Note objects.
It supports adding, searching, deleting, and displaying notes, with optional filtering by tags.
"""

from typing import List
from collections import UserList
from notes import Note
from display import StylizedElements, ColorsConstants


class Notebook(UserList):
    """
    A class for managing a collection of Note instances.
    """

    def add(self, note: Note):
        """Add a new note to the notebook."""
        self.data.append(note)

    def find(self, term: str) -> List[Note]:
        """Find notes that contain the search term in their title.

        Args:
            term (str): The substring to search for in note titles.

        Returns:
            list[Note]: A list of matching Note instances.
        """
        return [note for note in self.data if term in note.title.value]

    def find_by_tag(self, tag: str) -> List[Note]:
        """Find notes that contain a specific tag.

        Args:
            tag (str): The tag to filter notes by.

        Returns:
            list[Note]: Notes that have the specified tag.
        """
        return [
            note
            for note in self.data
            if any(note_tag for note_tag in note.tags if note_tag.value == tag)
        ]

    def delete(self, note: Note):
        """Remove a specific note from the notebook."""
        return self.data.remove(note)

    def is_empty(self):
        """Check if the notebook has no notes.

        Returns:
            bool: True if the notebook is empty, False otherwise."""
        return len(self.data) == 0

    def __str__(self):
        """Return a stylized string representation of the notebook.

        Returns:
            str: An empty string (since notes are printed directly via rich styling).
        """
        if self.is_empty():
            StylizedElements.stylized_print(
                "Notebook is empty", style=ColorsConstants.ERROR_COLOR.value
            )
            return ""

        StylizedElements.stylized_print(
            f'NoteBook:\n{'\n'.join(f"Title: {str(note.title)}\nText: {str(note.text)}\n ---" for note in self.data)}',
            style=ColorsConstants.HEADER_COLOR.value,
        )

        return ""
