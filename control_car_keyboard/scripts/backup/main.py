from pynput.keyboard import Key, Listener
import time
import rospy
import sys,tty,termios
from std_msgs.msg import String
from std_msgs.msg import Float32

t = time.time()

def on_press(key):
    pressValue = format(key)
    speed = 50
    if key == Key.up:
        runtime = str(time.time() - t)[0:5]
        rospy.loginfo(speed)
        pub_speed.publish(50)
        pub_angle.publish(0)
        print("press time: ",runtime)

    elif key == Key.left:
        runtime = str(time.time() - t)[0:5]
        set_angle = 2 + float(runtime) /0.1*1.5
        print("setAngle: ", set_angle)
        #pub_speed.publish(abs(speed - set_angle))
        pub_angle.publish(-set_angle)
	pub_speed.publish(50)

    elif key == Key.right:
        runtime = str(time.time() - t)[0:5]
        set_angle = 2 + float(runtime) /0.1*1.5
        print("setAngle: ", set_angle)
        pub_angle.publish(set_angle)
        #pub_speed.publish(abs(speed - set_angle))
	pub_speed.publish(50)

    elif key == Key.down:
        runtime = str(time.time() - t)[0:5]
        rospy.loginfo(speed)
        pub_speed.publish(0)
        #pub_angle.publish(0)



def on_release(key):
    global t
    t = time.time()
    pub_speed.publish(50)
    pub_angle.publish(0)
    print('=======================================')
    if key == Key.esc:
        return False


def taker():
    global pub_speed, pub_angle
    pub_speed = rospy.Publisher('/team1/set_speed', Float32, queue_size=10) # Khoi tao node speed de phat di
    pub_angle = rospy.Publisher('/team1/set_angle', Float32, queue_size=10) # Khoi tao node angle de phat di
    rospy.init_node('set_speed_control', anonymous=True) # Khai bao rospy name cua node

    while not rospy.is_shutdown():
        global t
        t = time.time()  # reading time in sec
        with Listener(on_press=on_press,
                      on_release=on_release) as listener:
            listener.join()

if __name__ == '__main__':
    try:
        taker()
    except rospy.ROSInterruptException:
        print("Exception for ROS")
