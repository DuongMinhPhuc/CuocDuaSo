import datetime

from pynput import keyboard
import time



def on_key_release(key):
    #print(key)
    time_run = time.time() - start_time
    print("time: ",time.time() - start_time)
    print("type: ",type(time_run))
    pass

def key_press(key):
    global start_time
    start_time = time.time()

with keyboard.Listener(on_release = on_key_release,on_press=key_press) as listener:
    listener.join()