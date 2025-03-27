from field import Field

class Name(Field):
    def _validate(self, value):
        if not value.strip():
            raise ValueError('Name cannot be empty')