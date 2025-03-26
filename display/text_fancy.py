import pyfiglet
from rich.console  import Console
from rich.text import Text

from .constants import ColorsConstants

def text_fancy(text:str)->None:
    console = Console()
    text = Text(pyfiglet.figlet_format(text))
    text.stylize(ColorsConstants.HEADER_COLOR.value)
    console.print(text)