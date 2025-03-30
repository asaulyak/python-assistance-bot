"""This module defines the NoteFindCommand class, which allows users to search for notes
in the notebook either by their title or by a specific tag.
Results are displayed in a stylized format using the StylistElements utility.
"""

from typing import List

from command.command import Command
from display.paginator import Paginator
from execution_context import ExecutionContext
from notes import Title, Tag, Note
from display import StylizedElements, ColorsConstants, TableBuilder


class NoteFineCommand(Command):
    """A command class that enables searching notes by either title or tag."""

    @property
    def name(self):
        return "find-note"

    @property
    def aliases(self):
        return ["fn"]

    @property
    def description(self):
        return "Find a note by title or tag"

    def run(self, _, context: ExecutionContext, __) -> bool:
        options = [Title.__name__, Tag.__name__]
        stop = False

        paginator = Paginator(options)
        option_index = paginator.show('Select a field to search')

        if option_index is None:
            return False


        field_name = options[option_index]
        term = StylizedElements.stylized_input(
            f"Type {field_name}: ", ColorsConstants.INPUT_COLOR.value
        )

        notes: List[Note] = []

        if option_index == 0:
            notes = context.notebook.find(term)
        elif option_index == 1:
            notes = context.notebook.find_by_tag(term)

        if not notes:
            StylizedElements.stylized_print(
                "Nothing found", ColorsConstants.WARNING_COLOR.value
            )
            return stop

        table_title = "Matching Notes"
        table_headers = ("Title", "Text", "Tags")
        table_data = [
            (
                note.title.value,
                note.text.value if note.text else "",
                ", ".join(tag.value for tag in note.tags),
            )
            for note in notes
        ]

        table = TableBuilder()
        table.set_title(table_title)
        table.set_table_headers(table_headers)
        table.set_table_data(table_data)
        table.set_highlight_text(term)
        table.show()

        return stop
