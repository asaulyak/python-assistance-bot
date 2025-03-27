from datetime import datetime
from field import Field


class Birthday(Field):
    def _validate(self, value):
        try:
            birthday = datetime.strptime(value, "%d.%m.%Y")

            now = datetime.now()
            is_in_future = birthday > now

            if is_in_future:
                raise IndexError("Birthday can't be in the future")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


