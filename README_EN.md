# Python Bot

This project implements a modular console bot using the Command design pattern, providing flexibility, scalability, and ease of adding new functionalities as individual commands.

## Project Architecture

The project follows a modular architecture to ensure clarity and ease of expansion.

### Visual Project Structure

```
python-assistance-bot/
├── address_book/
│   ├── __init__.py
│   ├── address.py
│   ├── address_book.py
│   ├── birthday.py
│   ├── email.py
│   ├── name.py
│   ├── phone.py
│   └── record.py
├── command/
│   ├── commands/
│   │   ├── add_command.py
│   │   ├── birthdays_command.py
│   │   ├── edit_command.py
│   │   ├── exit_command.py
│   │   ├── find_command.py
│   │   ├── hello_command.py
│   │   ├── help_command.py
│   │   ├── note_add_command.py
│   │   ├── note_delete_command.py
│   │   ├── note_edit_command.py
│   │   ├── note_find_command.py
│   │   ├── note_show_all_command.py
│   │   ├── notes_add_tag_command.py
│   │   ├── remove_command.py
│   │   ├── save_command.py
│   │   └── show_all_command.py
│   ├── command.py
│   └── command_runner.py
├── display/
│   ├── __init__.py
│   ├── constants.py
│   ├── paginator.py
│   ├── stylized_elements.py
│   └── table_builder.py
├── field/
│   ├── __init__.py
│   ├── empty_field.py
│   ├── field.py
│   └── initialisation.py
├── notes/
│   ├── __init__.py
│   ├── note.py
│   ├── notebook.py
│   ├── tag.py
│   ├── text.py
│   └── title.py
├── user_input/
│   ├── __init__.py
│   └── user_input.py
├── execution_context.py
├── main.py
├── persistence.py
├── requirements.txt
└── README.md
```

See details on [GitHub](https://github.com/asaulyak/python-assistance-bot).

### Command Module

The main logic for managing commands is implemented using the **Command** design pattern.

- **Command loading** occurs automatically during application initialization.
- **Adding new commands**:
  1. Create a new file in the `commands` directory.
  2. Implement a command class that inherits from the base `Command` class.

The command class should include:

- **`name`**: a unique string identifier used to call the command.
- **`aliases`** (optional): a list of alternative command names.
- **`description`**: detailed description displayed in help.

### Independent Modules

The notes and address book functionalities are implemented as separate modules:

- **Notes** — inherits from `UserList`.
- **Address Book** — inherits from `UserDict`.

This structure facilitates code reuse and simplifies maintenance.

### Input/Output Modules

Separate modules provide a consistent interaction style with the user:

- **User input handling**
- **Formatting and user output**

These modules standardize information display and user interactions.

## Advantages

- Modular architecture simplifies maintenance and expansion.
- The **Command** pattern allows easy addition of new commands without altering the main logic.
- Independent modules facilitate code reuse.
- Standardized input/output modules provide a unified user interface.

## Getting Started

1. Install project dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python main.py
```

3. Use the `help` command to see available commands and their descriptions.
