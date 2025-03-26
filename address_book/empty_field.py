from address_book import Field


class EmptyField(Field):
    def is_empty(self):
        return True