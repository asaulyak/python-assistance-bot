from command.command import Command
from display import ColorsConstants, StylizedElements
from execution_context import ExecutionContext
from field import init_field
from notes import Tag, Note


class AddTagNoteCommand(Command):
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
        # paginator = Paginator(context.notebook)

        # paginator.show()

        # index = index_question(
        #     "Type an index of a note to edit (or 'q' to cancel): ",
        #     max_index=len(context.notebook) - 1,
        # )

        # if index is None:
        #     StylizedElements.stylized_print(
        #         "No tags added", ColorsConstants.ERROR_COLOR.value
        #     )

        #     return False

        # while True:
        #     tag = init_field(Tag, input("Provide a tag: "))

        #     if tag and not tag.is_empty():
        #         break

        # note = context.notebook[index]

        # note.add_tag(tag)

        # message = f"Added tag to note: {note}"

        # StylizedElements.stylized_print(message)

        # return False
        stop = False
        notebook = context.notebook

        if notebook.is_empty():
            StylizedElements.stylized_print(
                "No notes available. Please add a note first.",
                ColorsConstants.WARNING_COLOR.value,
            )
            return stop

        note_options = [
            f"{i + 1}. {note.get_title().value}" for i, note in enumerate(notebook)
        ]
        note_options.append("Cancel")

        selected = StylizedElements.console_menu(
            "Select a note to add a tag:", note_options
        )

        if selected == "Cancel":
            return stop

        selected_index = note_options.index(selected)
        note: Note = notebook[selected_index]

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
