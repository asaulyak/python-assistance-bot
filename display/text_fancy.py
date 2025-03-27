import pyfiglet
from rich.text import Text
from .constants import ColorsConstants
from .stylized_print import stylized_print

def text_fancy(text:str)->None:
    """
    Prints a given text string in a stylized format using pyfiglet library
    
    Parameters:
    text (str): The text string to be printed in a stylized format
    """
    text = Text(pyfiglet.figlet_format(text))
    text.stylize(ColorsConstants.HEADER_COLOR.value)
    stylized_print(text)