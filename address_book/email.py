from field import Field
import re

class Email(Field):
    def _validate(self, value):
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value)

        if not valid:
            raise ValueError('Email is not valid')