from pynput import keyboard
import threading

_exit_function = None

def exit_program():
    print("ctrl+c exit")
    exit(0)


def hotkey_thread_function(name):
    with keyboard.GlobalHotKeys({
            '<27>': _exit_function, #27 = ESC
            '<ctrl>+c': exit_program}) as h: 
        h.join()


def listen_to_hotkeys(exit_function):
    global _exit_function
    _exit_function = exit_function
    hotkey_thread = threading.Thread(target=hotkey_thread_function, args=(1,))
    hotkey_thread.start()
    pass


