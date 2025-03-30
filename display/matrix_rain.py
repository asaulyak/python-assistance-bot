import os
import subprocess
import platform
import time
from pynput import keyboard
from typing import Optional

def matrix_rain(delay: Optional[int] = 5):
    """
    Displays a matrix rain effect using the pymatrix-rain library.
    Stops when 'q' is pressed or after a delay.
    """
    
    # Determine the clear command based on the platform
    CLEAR = 'cls' if platform.system() == "Windows" else 'clear'
    os.system(CLEAR)
    time.sleep(0.05)

    # Start the pymatrix-rain process
    if platform.system() == "Windows":
        process = subprocess.Popen(["pymatrix-rain"])
    else:
        process = subprocess.Popen(["cmatrix"])

    start_time = time.time()  # Record start time
    stop_flag = False 

    def on_press(key):
        nonlocal stop_flag
        try:
            if key.char == 'q':  # Stop if 'q' is pressed
                stop_flag = True
                return False  # Stop listener
        except AttributeError:
            pass  # Ignore special keys

    # Define the keyboard listener function
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    try:
        while True:
            if stop_flag:
                break
   
            # Stop if delay time has passed
            if time.time() - start_time >= delay:
                break

            time.sleep(0.1)  # Small delay to prevent high CPU usage

    finally:
        # Terminate the pymatrix-rain process
        process.terminate()
        time.sleep(0.05)
        listener.stop()
        time.sleep(0.05)
        process.kill()
        time.sleep(0.05)
        os.system(CLEAR)
        time.sleep(0.05)
        os.system("reset")



