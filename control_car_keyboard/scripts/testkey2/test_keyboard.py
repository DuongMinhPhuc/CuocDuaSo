from pynput.keyboard import Key, Listener
import sys,tty,termios
#https://stackoverflow.com/questions/22397289/finding-the-values-of-the-arrow-keys-in-python-why-are-they-triples
#https://pythonhosted.org/pynput/keyboard.html
import time

class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                print("up")
        elif k=='\x1b[B':
                print("down")
        elif k=='\x1b[C':
                print("right")
        elif k=='\x1b[D':
                print("left")
        # else:
        #         print("not an arrow key!")
start_time = time.time()

elapsed_time = time.time()

def on_press(key):
    global start_time
    # if format(key) == Key.up or Key.down or Key.left or Key.right:
    # #if format(key) == Key.up | Key.down | Key.left | Key.right:
    #     print('{0} pressed'.format(key))
    inkey = _Getch()
    while (1):
        k = inkey()
        if k != '': break
    if k == '\x1b[A':
        print("up")
    elif k == '\x1b[B':
        print("down")
    elif k == '\x1b[C':
        print("right")
    elif k == '\x1b[D':
        print("left")

def on_release(key):
    global elapsed_time
    # if format(key) == Key.up or Key.down or Key.left or Key.right :
    #     print('{0} pressed'.format(key))
    # if key == Key.esc:
    #     # Stop listener
    #     return False

    inkey = _Getch()
    while (1):
        k = inkey()
        if k != '': break
    if k == '\x1b[A':
        print("up release time ="+ str(elapsed_time - start_time))
    elif k == '\x1b[B':
        print("down release time ="+ str(elapsed_time - start_time))
    elif k == '\x1b[C':
        print("right release time = "+ str(elapsed_time - start_time))
    elif k == '\x1b[D':
        print("left release time ="+ str(elapsed_time - start_time))

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()