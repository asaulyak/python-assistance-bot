from field import Field, EmptyField


def init_field(constructor: type(Field), value: str | None) -> Field | None:
    if value == '':
        return EmptyField(value)

    if not value:
        return None

    try:
        return constructor(value)
    except Exception as e:
        print(str(e))

        return None