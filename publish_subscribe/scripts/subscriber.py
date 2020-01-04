#!/usr/bin/env python
import rospy
from std_msgs.msg import String

#check = 0

def callback(data):
    global check
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print("data " ,data.data)
    #check =


def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()