from pynput import keyboard
import time
#https://stackoverflow.com/questions/40649634/determine-length-of-keypress-in-python

def callb_release(key): #what to do on key-release
    ti1 = str(time.time() - t)[0:5] #converting float to str, slicing the float
    print("The key",key," is pressed for",ti1,'seconds')
    return False #stop detecting more key-releases
def callb_press(key): #what to do on key-press
    #pub du lieu realtime
    #while
    return False #stop detecting more key-presses

t = time.time() #reading time in sec
with keyboard.Listener(on_press = callb_press) as listener1: #setting code for listening key-press
    listener1.join()

with keyboard.Listener(on_release = callb_release) as listener: #setting code for listening key-release
    listener.join()

