from typing import List
from execution_context import ExecutionContext


class Command:
    def __init__(self):
        pass


    @property
    def name(self):
        return 'empty'


    @property
    def aliases(self):
        return []


    @property
    def description(self):
        return 'default description'


    def run(self, args: list[str], context: ExecutionContext, commands: List) -> [str, bool]:
        pass
