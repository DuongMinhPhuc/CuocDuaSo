
from pynput.keyboard import Key, Listener
import time

start_time = time.time()

def on_key_release(key):
    #print(key)
    global start_time
    print('start_time ',start_time)
    print('time.time() ',time.time())
    time_run = time.time() - start_time
    print("time: ",time.time() - start_time)
    return False

def key_press(key):
    global start_time
    start_time = time.time()
    return False

with Listener(
        on_press=key_press,
        on_release=on_key_release) as listener:
    listener.join()