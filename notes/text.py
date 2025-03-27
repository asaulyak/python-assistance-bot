from field import Field


class Text(Field):
    def _validate(self, value: str):
        if not value:
            raise ValueError('Please provide a text')

        if len(value.strip()) < 3:
            raise ValueError('Text should be at least 3 characters long')
