from field import Field

class Address(Field):
    def _validate(self, value):
        if len(value.strip()) < 3:
            raise ValueError('Address should be at least 3 characters long')