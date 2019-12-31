from pynput import keyboard 
import time
import sys,tty,termios

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
                return "up"
        elif k=='\x1b[B':
                print("down")
                return "down"
        elif k=='\x1b[C':
                print("right")
                return "right"
        elif k=='\x1b[D':
                print("left")
                return "left"
        # else:
        #         print("not an arrow key!")

def callb(key,t): #what to do on key-release
    ti1 = str(time.time() - t)[0:10] #converting float to str, slicing the float
    print(" is pressed for",ti1,'seconds')
    key = get()
    if key == "up":
        speed = 50
        rospy.loginfo(speed)
        pub_speed.publish(speed)
        print("up access")
    if key == "down":
        speed = 0
        rospy.loginfo(speed)
        pub_speed.publish(speed)
        print("down access")
    if key == "left":
        pub_angle.publish(-5)
        print("left access")
    if key == "right":
        pub_angle.publish(5)
        print("right access")
    if key != "left" and key != "right" and key != "up" and key != "down":
        pub_angle.publish(0)
    return False #stop detecting more key-releases
def callb1(key): #what to do on key-press
    return False #stop detecting more key-presses

with keyboard.Listener(on_press = callb1) as listener1: #setting code for listening key-press
    listener1.join()

t = time.time() #reading time in sec

with keyboard.Listener(on_release = callb) as listener: #setting code for listening key-release
    listener.join()