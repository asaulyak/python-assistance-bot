from persistence import load_data
from command.command_runner import CommandRunner
from user_input import yes_no_question
from display import text_fancy




def parse_command(user_input):
    if not user_input:
        return 'not_a_command', []

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


def main():
    context = load_data()

    # print("Welcome to the assistant bot!")
    text_fancy("Welcome to the assistant bot !")
    

    command_parser = CommandRunner()

    while True:
        fix_typo = input("Enter a command: ")
        cmd, *args = parse_command(fix_typo)

        command = command_parser.find_command(cmd)

        if not command:
            match = command_parser.find_suggested_command(cmd)

            if match:
                # this will return command because a match was found
                command = command_parser.find_command(match)

                fix_typo = yes_no_question(f"Did you mean '{match}{" ".join(args)}'?")

                if not fix_typo:
                    continue
            else:
                print('Command not found')
                continue


        commands_set = list(set(command_parser.commands.values()))
        message, stop = command.run(args, context, commands_set)

        # print(message)
        text_fancy(message)

        if stop:
            break


if __name__ == "__main__":
    main()