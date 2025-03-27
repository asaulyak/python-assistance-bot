def yes_no_question(question: str) -> bool:
    response = input(f'{question} Y/n ')

    return not response or response.lower() == 'y'


def index_question(question: str, max_index: int, min_index: int = 0, offer_quit = True) -> int | None:
    response = input(question)

    def input_index(user_input):
        while not user_input.isdigit():
            user_input = input('Number is expected: ')

        return int(response)

    if offer_quit and response.lower() == 'q':
        # stop interaction and return
        return None

    index = input_index(response)

    while index > max_index or index < min_index:
        response = input(f'Index should be in range from {min_index} to {max_index}: ')
        index = input_index(response)

    return index