from pynput.keyboard import Listener
import datetime
from pynput import keyboard
import time

check = True

def on_key_release(key):
    #print(key)
    global check
    global start_time
    time_run = time.time() - start_time
    print("time: ",time.time() - start_time)
    # print("type: ",time_run)
    print("key relsease")
    pass

def key_press(key):
    global check
    global start_time
    print("keypress")
    start_time = time.time()


with keyboard.Listener(on_release = on_key_release,on_press=key_press) as listener:
    listener.join()