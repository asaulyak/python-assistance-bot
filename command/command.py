from typing import List
from execution_context import ExecutionContext


class Command:
    @property
    def name(self):
        return 'empty'


    @property
    def aliases(self):
        return []


    @property
    def description(self):
        return 'default description'


    def run(self, args: list[str], context: ExecutionContext, commands: List) -> bool:
        pass
