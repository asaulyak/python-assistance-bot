from address_book.persistence import load_data
from command.command_runner import CommandRunner
from display import text_fancy,autocomplete




def parse_command(user_input):
    if not user_input:
        return 'not_a_command', []

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


def main():
    
    book = load_data()

    # print("Welcome to the assistant bot!")
    text_fancy("Welcome to the assistant bot !")
    # autocomplete()

    command_parser = CommandRunner()

    while True:
        user_input = input("Enter a command: ")
        cmd, *args = parse_command(user_input)

        command = command_parser.find_command(cmd)

        if not command:
            match = command_parser.find_suggested_command(cmd)

            if match:
                # this will return command because a match was found
                command = command_parser.find_command(match)

                user_input = input(f"Did you mean {match} {" ".join(args)}? y/n")
                if user_input != 'y':
                    continue
            else:
                print('Command not found')
                continue


        commands_set = list(set(command_parser.commands.values()))
        message, stop = command.run(args, book, commands_set)

        print(message)

        if stop:
            break


if __name__ == "__main__":
    main()