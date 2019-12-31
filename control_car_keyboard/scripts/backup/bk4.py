#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import sys,tty,termios
#rosrun control main.py

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
        elif k == "a":
            print("cua trai")
            return "a"
        elif k == "d":
            print("cua phai")
            return "d"
        # else:
        #         print("not an arrow key!")



def talker():
    pub_speed = rospy.Publisher('/team1/set_speed', Float32, queue_size=10)
    pub_angle = rospy.Publisher('/team1/set_angle', Float32, queue_size=10)
    rospy.init_node('set_speed_control', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
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
        if key == "a":
            pub_angle.publish(-25)
            print("cua trai")
        if key == "b":
            pub_angle.publish(25)
            print("cua phai")
        if key != "left" and key != "right" and key != "up" and key != "down" :
            pub_angle.publish(0)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass