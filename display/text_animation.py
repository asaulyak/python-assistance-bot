import time
import sys

def MatrixTextLoader(text, delay=0.05, line_wrap=60):
    """
    Displays text sequentially with Matrix-like styling.

    Parameters:
        text (str): The text to display.
        delay (float): Time delay between each character display (in seconds).
        line_wrap (int): Maximum number of characters per line before wrapping.
    """
    words = text.split()
    current_line = ''

    for word in words:
        # Check if adding the next word exceeds the line_wrap limit
        if len(current_line) + len(word) + 1 > line_wrap:
            # Print the current line character by character
            for char in current_line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            print()
            current_line = word + ' '
        else:
            current_line += word + ' '

    # Print remaining text
    for char in current_line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Final newline at the end

# if __name__ == "__main__":
#     sample_text = (
#         "Wake up, Neo... The Matrix has you... "
#         "Follow the white rabbit. Knock, knock, Neo."
#     )

#     matrix_text_loader(sample_text, delay=0.07, line_wrap=50)