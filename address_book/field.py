class Field:
    def __init__(self, value: str):
        self._validate(value)
        self.value = value


    def __str__(self):
        return str(self.value)


    def update(self, value):
        self._validate(value)

        self.value = value

    def is_empty(self):
        return False


    def _validate(self, value):
        pass