import os
import subprocess
import platform
import time
# from pynput import keyboard
from typing import Optional

def matrix_rain(delay: Optional[int] = 5):
    """
    Displays a matrix rain effect using the pymatrix-rain library.
    Stops when 'q' is pressed or after a delay.
    """
    
    # Determine the clear command based on the platform
    CLEAR = 'cls' if platform.system() == "Windows" else 'clear'
    os.system(CLEAR)

    # Start the pymatrix-rain process
    process = subprocess.Popen(["pymatrix-rain"])

    start_time = time.time()  # Record start time
# Flag to track 'q' key press

    # Define the keyboard listener function
    try:
        while True:
   
            # Stop if delay time has passed
            if time.time() - start_time >= delay:
                break

            time.sleep(0.1)  # Small delay to prevent high CPU usage

    finally:
        # Terminate the pymatrix-rain process
        process.terminate()
        process.kill()
        os.system(CLEAR)



