from display import StylizedElements, ColorsConstants
from rich.text import Text
from rich.console import Console

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