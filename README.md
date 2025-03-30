# Python Bot

Цей проєкт реалізує консольний бот із модульною архітектурою, який використовує шаблон Command. Він забезпечує гнучкість, масштабованість та зручність додавання нових функцій у вигляді окремих команд.

## Архітектура проєкту

Проєкт побудований на модульній архітектурі для забезпечення чіткої структури та простоти розширення.

### Візуальна структура проєкту

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

Детальніше дивіться на [GitHub](https://github.com/asaulyak/python-assistance-bot).

### Модуль Command

Основна логіка керування командами реалізована за допомогою шаблону проєктування **Command**.

- **Завантаження команд** здійснюється автоматично під час ініціалізації застосунку.
- **Додавання нових команд**:
  1. Створіть новий файл у директорії `commands`.
  2. Реалізуйте клас команди, успадковуючи його від базового класу `Command`.

Клас команди повинен містити:

- **`name`**: унікальний строковий ідентифікатор для виклику команди.
- **`aliases`** (опціонально): список альтернативних назв команди.
- **`description`**: детальний опис команди, що відображається в довідці (`help`).

### Незалежні модулі

Функціонал нотаток та адресної книги реалізовано у вигляді окремих модулів:

- **Нотатки** — успадковуються від `UserList`.
- **Адресна книга** — успадковується від `UserDict`.

Це дозволяє повторно використовувати код та спрощує підтримку.

### Модулі введення/виведення

Для забезпечення єдиного стилю взаємодії з користувачем створені окремі модулі:

- **Обробка введення (user input)**
- **Форматування та виведення (user output)**

Ці модулі стандартизують відображення інформації та взаємодію користувача з ботом.

## Переваги

- Модульна архітектура полегшує підтримку і розширення.
- Шаблон **Command** дозволяє легко додавати нові команди без зміни загальної логіки.
- Незалежні модулі забезпечують зручність повторного використання коду.
- Стандартизовані модулі введення/виведення надають єдиний інтерфейс взаємодії з користувачем.

## Початок роботи

1. Встановіть залежності проєкту:

```bash
pip install -r requirements.txt
```

2. Запустіть застосунок:

```bash
python main.py
```

3. Використовуйте команду `help`, щоб побачити список доступних команд та їх опис.

---

# [English Version](README_EN.md)

An English version of this README is available [here](README_EN.md).
