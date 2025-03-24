from address_book.persistence import load_data
from command.command_parser import CommandParser


def main():
    book = load_data()

    print("Welcome to the assistant bot!")

    command_parser = CommandParser()

    while True:
        user_input = input("Enter a command: ")
        cmd, *args = command_parser.parse_command(user_input)

        command = command_parser.find_command(cmd)

        if not command:
            command = command_parser.find_alias_command(cmd)

            if command:
                user_input = input(f"Did you mean {command.name} {" ".join(args)}? y/n")

                if user_input != 'y':
                    command = command_parser.find_suggested_command(cmd)

            else:
                command = command_parser.find_suggested_command(cmd)

                if command:
                    user_input = input(f"Did you mean {command.name} {" ".join(args)}? y/n")

                    if user_input != 'y':
                        continue
                else:
                    print('Command not found')
                    continue



        message, stop = command.run(args, book)

        print(message)

        if stop:
            break


if __name__ == "__main__":
    main()