from typing import List

from command.command import Command
from execution_context import ExecutionContext

from note_book import NoteBook, Note, Title, Body
from address_book.empty_field import EmptyField
from address_book import Field

class AddCommand(Command):
  @property
  def name(self):
    return 'add_note'
  
  @property
  def aliases(self):
    return ['create_note', 'new_note']
  
  @property
  def description(self):
    return 'Adds a new note to notebook'
  
  def run(self, args: list[str], context: ExecutionContext, commands: List) -> {str, bool}:
    args_len = len(args)

    title = None
    body = None

    # # get note details from args if passed
    # title = None if args_len < 1 else self.__init_field(Title, args[0])

    while not title:
      title = self.__init_field(Title, input('Title:'))

    while not body:
       body = self.__init_field(Body, input("Body:"))

    note = context.note.find(title, Note(title))

    if body and not body.is_empty():
       note.add_body(body)
      
    message = "Note added"

    context.note.add_note(note)

    return message, False


  def __init_field(self, constructor: type(Field), value: str | None) -> Field | None:
    if value == '':
        return EmptyField(value)

    if not value:
        return None

    try:
        return constructor(value)
    except Exception as e:
        print(str(e))

        return None