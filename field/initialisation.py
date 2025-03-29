from field import Field, EmptyField
from display import ColorsConstants,StylizedElements


def init_field(constructor: type(Field), value: str | None) -> Field | None:
    if value == '':
        return EmptyField(value)

    if not value:
        return None

    try:
        return constructor(value)
    except Exception as e:
        
        StylizedElements.stylized_print(str(e), ColorsConstants.ERROR_COLOR.value)

        return None