from persistence import load_data
from command.command_runner import CommandRunner
from user_input import yes_no_question,autocomplete_text
from display import StylizedElements, ColorsConstants, matrix_rain
from rich.text import Text


def parse_command(user_input):
    if not user_input:
        return 'not_a_command', []

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


def main():
    context = load_data()
    matrix_rain()
    StylizedElements.fancy_text("Follow the white rabbit")
    command_parser = CommandRunner()

    while True:
        
        main_commands = {key:value for key,value in command_parser.commands.items() if key not in  value.aliases}.keys()
        fix_typo = autocomplete_text(main_commands)

        cmd, *args = parse_command(fix_typo)

        command = command_parser.find_command(cmd)

        if not command:
            match = command_parser.find_suggested_command(cmd)

            if match:
                # this will return command because a match was found
                command = command_parser.find_command(match)
                # colorized text
                text = Text()
                text.append("Did you mean ", style=ColorsConstants.INPUT_COLOR.value)
                text.append(f"'{match}{" ".join(args)}' ",
                            style=ColorsConstants.HIGHLIGHT_COLOR.value)
                text.append("?", style=ColorsConstants.INPUT_COLOR.value)
                fix_typo = yes_no_question(text)

                if not fix_typo:
                    continue
            else:
                StylizedElements.stylized_print('Command not found',
                                                ColorsConstants.ERROR_COLOR.value)
                continue


        commands_set = list(set(command_parser.commands.values()))
        stop = command.run(args, context, commands_set)

        if stop:
            break


if __name__ == "__main__":
    main()