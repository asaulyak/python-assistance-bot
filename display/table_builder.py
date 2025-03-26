import re

from typing import Self,List,Tuple

from rich import box
from rich.console import Console
from rich.table import Table
from rich.text import Text

from fancify_text import wide,monospaced
from .constants import ColorsConstants as Colors,TableSettings

class TableBuilder:
    '''
    Table Builder    
    '''
    def __init__(self:Self,
                 table_title:str = '',
                 table_headers:Tuple[str] = (),
                 table_data:List[Tuple[str]]=[],
                 highlight:str = '',
                 sort_by_header:str = '')->None:
        self.__table = Table(
            title=table_title.capitalize(),
            show_lines=True,
            header_style="bold",
            row_styles=[Colors.ROW_COLOR.value],
            box=box.SQUARE_DOUBLE_HEAD,
            min_width=TableSettings.TABLE_MIN_WIDTH.value

            )
        self.__message = ''
        self.__build_table(table_headers,table_data, highlight,sort_by_header)
        self.__show__()

    def __build_table(self:Self,table_headers:Tuple[str],
                      table_data:List[Tuple[str]],highlight:str,sort_by_header:str)->None:
        # check if table is empty
        if  len(table_headers) == 0 or len(table_data) == 0:
            self.__message = 'Table is empty'
            return
        if not len(table_headers) == len(table_data[0]):
            self.__message = 'Number of headers columns and rows columns are not equal'
            return
        # table headers
        for header in table_headers:
            #highlight the header for sorting table
            header_style = Colors.HEADER_COLOR.value \
                if  header.lower() != sort_by_header.lower() else Colors.HIGHLIGHT_COLOR.value
            self.__table.add_column(
                Text(
                    wide(header.capitalize()),
                    style=header_style
                    ),
                justify=TableSettings.COLUMN_ALIGNMENT.value,  no_wrap=True,max_width=TableSettings.COLUMN_MAX_WIDTH.value)
        # table rows
        for row in table_data:
            if len(highlight) == 0:
                self.__table.add_row(*row)
                continue
            else:
                #highlight text in the row
                data = []
                for value in row:
                    text = Text(value)
                    pattern = re.compile(rf"{re.escape(highlight)}",re.IGNORECASE)
                    text.highlight_regex(pattern, Colors.HIGHLIGHT_COLOR.value)
                    data.append(text)
                self.__table.add_row(*tuple(data))

    def __show__(self:Self)->None:
        console = Console()
        if self.__table.columns:
            console.print(self.__table)
        else:
            console.print(monospaced(self.__message))

    def __str__(self:Self)->str:
        return "Class TableBuilder"