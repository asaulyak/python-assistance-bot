"""TODO:"""

from typing import Tuple

from command.command import Command
from execution_context import ExecutionContext


class NoteSortByTagCommand(Command):
    """TODO:"""

    @property
    def name(self):
        return "sort-note-by-tag"

    @property
    def aliases(self):
        return ["stn", "sorttag"]

    @property
    def description(self):
        return "Sort notes by passed tags"

    def run(self, _, context: ExecutionContext, __) -> Tuple[str, bool]:
        pass
