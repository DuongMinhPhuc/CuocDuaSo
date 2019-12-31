import keyboard
import time
shot_pressed = 0
try:
    while True:
        if keyboard.is_pressed("S"):
            shot_pressed += 1
            time.sleep(0.1)
            print(shot_pressed)
        print("run")
except Exception as er:
    print(er)