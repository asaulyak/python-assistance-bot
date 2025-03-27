from rich.console  import Console
from typing import Optional

def stylized_print(text:str, style:Optional[str] = '')->None:
    """Prints the given text with a specified style.
    If no style is given, just prints the text normally."""
    console = Console()
    console.print(text, style=style)