import re
from typing import Self,List,Tuple
from rich import box
from rich.table import Table
from rich.text import Text
from fancify_text import wide
from .constants import ColorsConstants as Colors,TableSettings
from .stylized_elements import StylizedElements

class TableBuilder:
    '''
    Table Builder    
    '''
    def __init__(self:Self)->None:
        self.__table_headers:Tuple[str,...] = ()
        self.__table_data:List[Tuple[str,...]] = []
        self.__highlight_text:str = ''
        self.__highlight_header:str = ''
        self.__message:str= ''
        self.__table:Table = Table(
            show_lines=True,
            header_style="bold",
            row_styles=[Colors.ROW_COLOR.value],
            box=box.SQUARE_DOUBLE_HEAD,
            min_width=TableSettings.TABLE_MIN_WIDTH.value
            )
        

    def __validate_table(self:Self)->bool:
        """
        Validates if the table headers and data are correctly set.
        """
        if not self.__table_headers or not self.__table_data:
            self.__message = 'Table are empty' if not self.__message else self.__message
            return False
        if  len(self.__table_headers) != len(self.__table_data[0]):
            self.__message = 'Number of headers columns and rows columns are not equal' if not self.__message else self.__message
            return False
        return True


    def __build_table(self:Self)->None:        
        """
        Builds the table by adding headers and rows.
        """
        # validate table data
        if not self.__validate_table():
            return
        
        # table headers
        for header in self.__table_headers:
            #highlight the header for sorting table
            header_style = (
                Colors.HIGHLIGHT_COLOR.value
                if header.lower() == self.__highlight_header.lower()
                else Colors.HEADER_COLOR.value
            )
            self.__table.add_column(
                Text(wide(header.capitalize()),style=header_style),
                justify=TableSettings.COLUMN_ALIGNMENT.value,
                no_wrap=True,
                max_width=TableSettings.COLUMN_MAX_WIDTH.value)
            
        # table rows
        for row in self.__table_data:
            if len(self.__highlight_text) == 0:
                self.__table.add_row(*row)
                continue            
            #highlight text in the row
            data = [self.__highlight_text_in_row(value) for value in row]
            self.__table.add_row(*tuple(data))

    def __highlight_text_in_row(self:Self,value:str)->Text:
        """
        Highlights matching text in a table cell.
        """
        text = Text(value)
        pattern = re.compile(rf"{re.escape(self.__highlight_text)}",re.IGNORECASE)
        text.highlight_regex(pattern, Colors.HIGHLIGHT_COLOR.value)
        return text

    def set_title(self: Self, title: str) -> None:
        """Sets the table title."""
        if isinstance(title, str) and title.strip():
            self.__table.title = title.strip().capitalize()
        else:
            StylizedElements.stylized_print("Invalid title", Colors.ERROR_COLOR.value)

    def set_table_headers(self: Self, table_headers: Tuple[str, ...]) -> None:
        """Sets the table headers."""
        if isinstance(table_headers, tuple) and table_headers:
            self.__table_headers = table_headers
        else:
            self.__message = "Invalid table headers"

    def set_table_data(self: Self, table_data: List[Tuple[str, ...]]) -> None:
        """Sets the table data."""
        if isinstance(table_data, list) and table_data:
            self.__table_data = table_data
        else:
            self.__message = "Invalid table data"

    def set_highlight_text(self: Self, highlight_text: str) -> None:
        """Sets the text to be highlighted in the table."""
        if isinstance(highlight_text, str) and highlight_text.strip():
            self.__highlight_text = highlight_text.strip()
        else:
            self.__message = "Invalid highlight text value"

    def set_highlight_header(self: Self, highlight_header: str) -> None:
        """Sets the text to be highlighted in the table header."""
        if isinstance(highlight_header, str) and highlight_header.strip():
            self.__highlight_header = highlight_header.strip()
        else:
            self.__message = "Invalid highlight header value"

    def show(self: Self) -> None:
        """Displays the table."""
        self.__build_table()
        if self.__table.columns:
            StylizedElements.stylized_print(self.__table)
        else:
            StylizedElements.stylized_print(self.__message, Colors.ERROR_COLOR.value)
        

    def __str__(self: Self) -> str:
        return "Class TableBuilder"