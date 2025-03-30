"""This module defines the NoteDeleteCommand, a CLI command that allows
users to delete a note from the notebook interactively.

The user is presented with a list of all existing note titles via a
console menu. Upon selecting a note (or canceling the operation), the
selected note is deleted from the notebook and a confirmation message
is displayed."""

from command.command import Command
from display.paginator import Paginator
from notes import Notebook
from display import StylizedElements, ColorsConstants
from execution_context import ExecutionContext


class NoteDeleteCommand(Command):
    """A command that allows users to delete an existing note from the notebook.

    This command displays a stylized interactive menu listing all notes by title,
    allowing the user to select one for deletion. If the user selects 'Cancel',
    the operation is aborted. If no notes exist, a warning is displayed."""

    @property
    def name(self):
        return "delete-note"

    @property
    def aliases(self):
        return ["dn"]

    @property
    def description(self):
        return "Delete note"

    def run(self, _, context: ExecutionContext, __) -> bool:
        notebook: Notebook = context.notebook
        stop = False

        if notebook.is_empty():
            StylizedElements.stylized_print(
                "No notes to delete. Please add a note first.",
                ColorsConstants.HIGHLIGHT_COLOR.value,
            )

            return stop

        notes = notebook.to_list()

        paginator = Paginator(notes)
        note_index = paginator.show('Select a note to delete')

        if note_index is None:
            return False

        note_to_remove = notebook[note_index]
        notebook.delete(note_to_remove)

        StylizedElements.stylized_print(
            f"Deleted note: {note_to_remove.get_title().value}",
            style=ColorsConstants.SUCCESS_COLOR.value,
        )

        return stop
