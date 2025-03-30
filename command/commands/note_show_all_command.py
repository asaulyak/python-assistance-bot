"""
This module defines the NoteShowAllCommand class, which provides functionality
to display all notes stored in the notebook in a formatted table.
"""

from command.command import Command
from display import StylizedElements, ColorsConstants, TableBuilder
from execution_context import ExecutionContext


class NoteShowAllCommand(Command):
    """A command class to display all notes in the user's notebook.

    Displays the notebook contents in a table format using rich styling."""

    @property
    def name(self):
        return "all-notes"

    @property
    def aliases(self):
        return ["alln"]

    @property
    def description(self):
        return "Show all notes"

    def run(self, _, context: ExecutionContext, __) -> bool:
        stop = False

        if context.notebook.is_empty():
            StylizedElements.stylized_print(
                "No notes available.", style=ColorsConstants.WARNING_COLOR.value
            )
            return stop

        table_title = "Notes 📝"
        table_headers = ("Title", "Text", "Tags")
        table_data = [note.table_data() for note in context.notebook.to_list()]

        table = TableBuilder()
        table.set_title(table_title)
        table.set_table_headers(table_headers)
        table.set_table_data(table_data)

        table.show()

        return stop
