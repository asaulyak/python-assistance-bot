import subprocess
import time
import platform
import os
import keyboard
from typing import Optional
def matrix_rain(delay:Optional[int]=5):
    '''
    Displays a matrix rain effect using the pymatrix-rain library.
    '''
    CLEAR = 'cls' if platform.system() == "Windows" else 'clear'
    os.system(CLEAR)

    process = subprocess.Popen(["pymatrix-rain"])

    start_time = time.time()    # Record the start time

    try:
        while True:

            if keyboard.is_pressed('q'):  # Check if 'q' is pressed
                break
            if time.time() - start_time >= delay:  # Check if enough time has passed
                break
            time.sleep(0.1)  # Small delay to prevent CPU overuse

    finally:
        process.terminate()  # Gracefully stop the process
        process.wait()  # Ensure it exits before proceeding