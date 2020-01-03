#!/usr/bin/env python
# license removed for brevity
import time
from pynput import keyboard
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import sys,tty,termios
#rosrun control main.py
check_press = False

class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
            print("OKKKKKKKK: ")
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
            # print("right")
            return "right"
    elif k=='\x1b[D':
            # print("left")
            return "left"
        # else:
        #         print("not an arrow key!")

def callb_release(key): #what to do on key-release
    #breake vong lap
    global check_press
    check_press = False
    print("key release")
    pub_angle.publish(0)
    return False #stop detecting more key-releases

def callb_press(key): #what to do on key-press
    global check_press
    check_press = True
    runtime = str(time.time() - t)[0:5]
    # ti1 = str(time.time() - t)[0:5]  # converting float to str, slicing the float
    # print("The key", key, " is pressed for", ti1, 'seconds')
    key = get()
    z = key
    while True:
        if key == "up":
            speed = 50
            runtime = str(time.time() - t)[0:5]
            rospy.loginfo(speed)
            pub_speed.publish(speed)
            pub_angle.publish(0)
            print("press time: ",runtime)
            break

        if key == "down":
            speed = 0
            runtime = str(time.time() - t)[0:5]
            rospy.loginfo(speed)
            pub_speed.publish(50)
            pub_angle.publish(180)
            print("press time: ",runtime)
            break

        if key == "left":
            check_left = True
            while check_left:
                print('ookokoko')
                print("truoc key board")
                # with keyboard.Listener(on_release=callb_release) as listener:  # setting code for listening key-release
                #     listener.join()
                print("sau keyboard")
                runtime = str(time.time() - t)[0:5]
                set_angle = float(runtime) /0.25*1.5
                print("setAngle: ", set_angle)
                pub_angle.publish(-set_angle)
                print("press time: ",runtime)
                z = get()
                if check_press == False or z != "left":
                    print(" break left right")
                    check_left = False
                    break
            # break

        if key == "right":
            check_right = True
            while check_right:
                print("truoc key board")

                # with keyboard.Listener(on_release=callb_release) as listener:  # setting code for listening key-release
                #     listener.join()
                print("sau keyboard")
                runtime = str(time.time() - t)[0:5]
                set_angle = float(runtime) /0.15*1.5
                print("setAngle: ", set_angle)
                pub_angle.publish(set_angle)
                print("press time: ", runtime)
                z = get()
                if check_press == False or z != "right":
                    check_right = False
                    print(" break left right")
                    break
        break

        if key != "left" and key != "right" and key != "up" and key != "down":
            pub_angle.publish(0)

            callb_press()

    #pub du lieu realtime
    #while
    return False #stop detecting more key-presses

t = time.time() #reading time in sec

def talker():
    global pub_speed, pub_angle
    pub_speed = rospy.Publisher('/team1/set_speed', Float32, queue_size=10) # Khoi tao node speed de phat di
    pub_angle = rospy.Publisher('/team1/set_angle', Float32, queue_size=10) # Khoi tao node angle de phat di

    rospy.init_node('set_speed_control', anonymous=True) # Khai bao rospy name cua node
    rate = rospy.Rate(100) # Toc do giao tiep la 10Hz
    while not rospy.is_shutdown():
        global t
        t = time.time()  # reading time in sec
        with keyboard.Listener(on_press=callb_press) as listener1:  # setting code for listening key-press
            listener1.join()

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
