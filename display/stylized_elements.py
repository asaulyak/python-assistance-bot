import pyfiglet
from rich.console  import Console
from rich.text import Text
from typing import Optional
from .constants import ColorsConstants

class StylizedElements:
    console = Console()
    @classmethod
    def stylized_print(cls, text:str, style:Optional[str] = '')->None:
        """Prints the given text with a specified style.
        If no style is given, just prints the text normally."""
        cls.console.print(text, style=style)
    @classmethod
    def stylized_input(cls, text:str, style:Optional[str] = '')->None:
        """Prints the given text with a specified style and waits for user input.
        If no style is given, just prints the text normally."""
        cls.console.input(Text(text, style=style))

    @classmethod
    def fancy_text(cls, text:str)->None:
        """Prints a given text string in a stylized format using pyfiglet library"""
        text = Text(pyfiglet.figlet_format(text))
        text.stylize(ColorsConstants.HEADER_COLOR.value)
        cls.console.print(text)