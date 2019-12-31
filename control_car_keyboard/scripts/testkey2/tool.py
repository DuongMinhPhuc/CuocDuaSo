from pynput import keyboard
import time

def callb_press(key): #what to do on key-press
    print("press")
    return False #stop detecting more key-presses

while True:
    with keyboard.Listener(on_release = callb_press) as listener1: #setting code for listening key-press
        listener1.join()