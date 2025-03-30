"""This module defines the AddTagNoteCommand class, a CLI command that enables users to add tags
to existing notes stored in the notebook.

The command presents an interactive menu for selecting a note and prompts the user to input
a tag, which is then validated and associated with the selected note. It leverages rich
console output and stylized elements for a user-friendly interface."""

from command.command import Command
from display import ColorsConstants, StylizedElements
from display.paginator import Paginator
from execution_context import ExecutionContext
from field import init_field
from notes import Tag, Note


class AddTagNoteCommand(Command):
    """A command to add a tag to an existing note in the user's notebook.

    This command uses a stylized console menu to allow the user to select
    a note by title. Once a note is selected, the user is prompted to enter
    a tag. The tag is validated and then attached to the selected note."""

    @property
    def name(self):
        return "add-tag-note"

    @property
    def aliases(self):
        return ["tag"]

    @property
    def description(self):
        return "Add tag to a note"

    def run(self, _, context: ExecutionContext, __) -> bool:
        stop = False
        notebook = context.notebook

        if notebook.is_empty():
            StylizedElements.stylized_print(
                "No notes available. Please add a note first.",
                ColorsConstants.WARNING_COLOR.value,
            )
            return stop

        notes = notebook.to_list()

        paginator = Paginator(notes)
        note_index = paginator.show('Select a note to add a tag')

        if note_index is None:
            return stop

        note: Note = notebook[note_index]

        # Prompt for tag
        while True:
            raw_tag = StylizedElements.stylized_input(
                "Provide a tag: ", ColorsConstants.INPUT_COLOR.value
            )
            tag = init_field(Tag, raw_tag)
            if tag and not tag.is_empty():
                break

        note.add_tag(tag)

        StylizedElements.stylized_print(
            f"Added tag to note: {note.get_title().value}",
            ColorsConstants.SUCCESS_COLOR.value,
        )

        return stop
