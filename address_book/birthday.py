from datetime import datetime
from .field import Field


class Birthday(Field):
    def _validate(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


