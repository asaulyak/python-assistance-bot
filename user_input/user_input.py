from typing import List
from rich.text import Text
from rich.console import Console
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style
from display import  ColorsConstants

def yes_no_question(question: str) -> bool:
    console = Console()
    styled_prompt = Text()
    styled_prompt.append(question)
    styled_prompt.append(' Y/n ', style=ColorsConstants.HIGHLIGHT_COLOR.value)
    response = console.input(styled_prompt)

    return not response or response.lower() == 'y'


def index_question(question: str, max_index: int, min_index: int = 0, offer_quit = True) -> int | None:
    response = input(question)

    def input_index(user_input):
        while not user_input.isdigit():
            user_input = input('Number is expected: ')

        return int(user_input)

    if offer_quit and response.lower() == 'q':
        # stop interaction and return
        return None

    index = input_index(response)

    while index > max_index or index < min_index:
        response = input(f'Index should be in range from {min_index} to {max_index}: ')
        index = input_index(response)

    return index


def autocompelete_text(commands:List[str]) -> str:
    '''
    Create a completer (auto-suggests commands)
    '''
    # Create a completer (auto-suggests commands)
    command_completer = WordCompleter(commands, ignore_case=True, sentence=True)
    our_style = Style.from_dict({
        "prompt": ColorsConstants.INPUT_COLOR.value,
        "completion-menu.completion": "bg:#333333 #ffffff",  # Suggestion text
        "completion-menu.completion.current": "bg:#00ff00 #000000",  # Highlighted selection
    })

    while True:
        user_input = prompt("Enter command: ", completer=command_completer, style=our_style,)

        return user_input