"""This module defines the NoteDeleteCommand, a CLI command that allows
users to delete a note from the notebook interactively.

The user is presented with a list of all existing note titles via a
console menu. Upon selecting a note (or canceling the operation), the
selected note is deleted from the notebook and a confirmation message
is displayed."""

from command.command import Command
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

        if notebook.is_empty():
            StylizedElements.stylized_print(
                "No notes to delete. Please add a note first.",
                ColorsConstants.HIGHLIGHT_COLOR.value,
            )

            return False

        options = [
            f"{i + 1}. {note.get_title().value}" for i, note in enumerate(notebook)
        ]
        options.append("Cancel")

        selected = StylizedElements.console_menu("Select a note to edit:", options)

        if selected == "Cancel":
            return False

        selected_index = options.index(selected)
        note_to_remove = notebook[selected_index]
        notebook.delete(note_to_remove)

        StylizedElements.stylized_print(
            f"Deleted note: {note_to_remove.get_title().value}",
            style=ColorsConstants.SUCCESS_COLOR.value,
        )

        return False
