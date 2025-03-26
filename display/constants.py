from enum import Enum

class ColorsConstants(Enum):
    HIGHLIGHT_COLOR = '#BF9545'
    HEADER_COLOR = '#45BF84'
    ROW_COLOR = '#45BF84'
    SUGGESTION_TEXT = '#6c757d'

    def __str__(self):
        return "Colors constants\n"

class TableSettings(Enum):
    COLUMN_ALIGNMENT = 'left'
    COLUMN_MAX_WIDTH = 30
    TABLE_MIN_WIDTH = 80

    def __str__(self):
        return "Table settings constants\n"