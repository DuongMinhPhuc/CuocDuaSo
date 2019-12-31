#!/usr/bin/env python
# license removed for brevity
import time

import rospy
from pynput import keyboard
from std_msgs.msg import String
from std_msgs.msg import Float32
import sys,tty,termios

check_press_btn = False

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
                #print("up")
                return "up"
        elif k=='\x1b[B':
                #print("down")
                return "down"
        elif k=='\x1b[C':
                #print("right")
                return "right"
        elif k=='\x1b[D':
                #print("left")
                return "left"
        # else:
        #         print("not an arrow key!")



def callb(key): #what to do on key-release
    key = get()
    global check_press_btn
    check_press_btn = True
    t = time.time()
    #runtime = str(time.time() - t)[0:7] #converting float to str, slicing the float
    print(" is pressed for",runtime,'seconds')
    if key == "up":
        speed = 50
        rospy.loginfo(speed)
        pub_speed.publish(speed)
        #print("up access")
    if key == "down":
        speed = 0
        rospy.loginfo(speed)
        pub_speed.publish(speed)
        #print("down access")
    if key == "left":
        while True:
            runtime = str(time.time() - t)[0:7]
            print("runtime: ",runtime)
            set_angle = -float(runtime)/0.5*5
            pub_angle.publish(set_angle)
            # neu key release thi dung callb
            with keyboard.Listener(on_release=callb1) as listener:  # setting code for listening key-release
                listener.join()
            if check_press_btn == False:
                print("break")
                break

        #print("left access")
    if key == "right":
        while True:
            runtime = str(time.time() - t)[0:7]
            print("runtime: ", runtime)
            set_angle = -float(runtime) / 0.5 * 5
            pub_angle.publish(set_angle)
            with keyboard.Listener(on_release=callb1) as listener:  # setting code for listening key-release
                listener.join()
            if check_press_btn == False:
                print("break")
                break
        #print("right access")
    if key != "left" and key != "right" and key != "up" and key != "down" :
        pub_angle.publish(0)
    return False #stop detecting more key-releases

def callb1(key): #what to do on key-press
    global check_press_btn
    check_press_btn = False
    return False #stop detecting more key-presses

def talker():
    global pub_speed, pub_angle
    pub_speed = rospy.Publisher('/team1/set_speed', Float32, queue_size=10)
    pub_angle = rospy.Publisher('/team1/set_angle', Float32, queue_size=10)
    rospy.init_node('set_speed_control', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # key = get()
        # if key == "up":
        #     speed = 50
        #     rospy.loginfo(speed)
        #     pub_speed.publish(speed)
        #     print("up access")
        # if key == "down":
        #     speed = 0
        #     rospy.loginfo(speed)
        #     pub_speed.publish(speed)
        #     print("down access")
        # if key == "left":
        #     pub_angle.publish(-5)
        #     print("left access")
        # if key == "right":
        #     pub_angle.publish(5)
        #     print("right access")
        # if key != "left" and key != "right" and key != "up" and key != "down" :
        #     pub_angle.publish(0)


        with keyboard.Listener(on_press=callb) as listener1:  # setting code for listening key-press
            listener1.join()



        # with keyboard.Listener(on_release=callb) as listener:  # setting code for listening key-release
        #     listener.join()

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass