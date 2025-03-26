from pynput.keyboard import Listener,Controller

keyboard = Controller()

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
def autocomplete() -> None:
    while True:
        with Listener(on_press=on_press) as listener:
            listener.join()
        