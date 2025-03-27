from field import Field


class Tag(Field):
    def _validate(self, value: str):
        if not value:
            raise ValueError('Please provide a tag')

        if len(value.strip()) < 2:
            raise ValueError('Tag should be at least 2 characters long')
