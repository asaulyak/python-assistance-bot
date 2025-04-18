
from enum import Enum

class ColorsConstants(Enum):
    MAIN_COLOR = '#0dbc79'
    HIGHLIGHT_COLOR = '#BF9545'
    HEADER_COLOR = '#0dbc79'
    ROW_COLOR = '#0dbc79'
    SOFT_COLOR = '#29734f'
    SUGGESTION_TEXT = '#6c757d'
    ERROR_COLOR = '#ff0000'
    SUCCESS_COLOR = '#0261fb'
    INPUT_COLOR = '#0dbc79'
    WARNING_COLOR = '#fbff08'

    def __str__(self):
        return "Colors constants\n"

class TableSettings(Enum):
    COLUMN_ALIGNMENT = 'left'
    COLUMN_MAX_WIDTH = 25
    TABLE_MIN_WIDTH = 80

    def __str__(self):
        return "Table settings constants\n"