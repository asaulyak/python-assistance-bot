from enum import Enum

class ColorsConstants(Enum):
    HIGHLIGHT_COLOR = '#BF9545'
    HEADER_COLOR = '#45BF84'
    ROW_COLOR = '#45BF84'
    SOFT_COLOR = '#29734f'
    SUGGESTION_TEXT = '#6c757d'
    ERROR_COLOR = '#ff0000'

    def __str__(self):
        return "Colors constants\n"

class TableSettings(Enum):
    COLUMN_ALIGNMENT = 'left'
    COLUMN_MAX_WIDTH = 25
    TABLE_MIN_WIDTH = 80

    def __str__(self):
        return "Table settings constants\n"