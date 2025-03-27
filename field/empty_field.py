from field import Field


class EmptyField(Field):
    def is_empty(self):
        return True