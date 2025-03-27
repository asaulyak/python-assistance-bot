from field import Field


class Title(Field):
    def _validate(self, value: str):
        if not value:
            raise ValueError('Please provide a title')

        if len(value.strip()) < 3:
            raise ValueError('Title should be at least 3 characters long')
