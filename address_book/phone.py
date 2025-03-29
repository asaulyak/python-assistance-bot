from field import Field

class Phone(Field):
    def _validate(self, value):
        valid = len(value) == 10 and value.isdigit()

        if not valid:
            raise ValueError('Phone should be 10 characters long and contain only digits')


    def __str__(self):
        return f'({self.value[:3]}) {self.value[3:6]}-{self.value[6:]}'


    def __eq__(self, other):
        return self.value == other.value


    def __hash__(self):
        return hash(self.value)