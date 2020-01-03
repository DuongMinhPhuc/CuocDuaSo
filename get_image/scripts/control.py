#! /usr/bin/python
import math

from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import CompressedImage
import rospy
import cv2
import numpy as np
# from lane_detect import pipeline
from PIL import Image
from segment_function import load_model_segmentation, segment_image
import numpy as np
import cv2
from draw_line_function import detect_line
import matplotlib.pyplot as plt
from std_msgs.msg import Float32

net = 0
COLORS = 0
count = 0
pub_speed = None
pub_angle = None

# 320*240
def slope(x1, y1, x2, y2): # Line slope given two points:
	# print(str(x1)+","+str(x2)+","+str(y1)+","+str(y2))
	# print(str(float(y2)-float(y1)) + "," + str(float(x2)-float(x1)))
	return (float(y2)-float(y1))/(float(x2)-float(x1))


def angle(s1, s2):
    return math.degrees(math.atan((float(s2)-float(s1))/(float(1)+(float(s2)*float(s1)))))


def callback_rgb(data):
	global count
	global net, COLORS
	bridge = CvBridge()
	try:
		np_arr = np.fromstring(data.data, np.uint8)
		cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
	except CvBridgeError as e:
		print(e)

	#test pub speed and angle

	#write image
	if count % 17 == 0:
		#show segmentation image
		segmentImage = segment_image(cv_image, net, COLORS)

		#get trung vi line detect
		list_y, list_x = detect_line(segmentImage)

		#drawl line trung vi

		for i in range(len(list_x)):
			segmentImage[int(list_x[i]), int(list_y[i])] = [0,0,255]

		for i in range(len(list_x)):
			cv_image[int(list_x[i]), int(list_y[i])] = [0,0,255]



		# control car
		# lay diem giua bottom anh va diem cuoi cung cua line detect => goc lech => dieu khien
		# 160*240
		bottomPointX = 160
		bottomPointY = 240


		#do duong thang tinh tu tren xuong
		lastLinePointX = int(list_x[0])
		print("lastLinePointX ",lastLinePointX)
		lastLinePointY = int(list_y[0])

		#drawl

		lineThickness = 5
		cv2.line(cv_image, (bottomPointX, 0), (bottomPointX, bottomPointY), (0, 255, 0), lineThickness)
		cv2.line(cv_image, (lastLinePointY,lastLinePointX), (bottomPointX, bottomPointY), (0, 255, 0), lineThickness)
		cv2.imshow("real image ", cv_image)
		cv2.imshow("segmentImage", segmentImage)
		cv2.waitKey(3)

		#tinh goc control
		# pub_angle.publish(180)
		pub_speed.publish(50)
		slope_detect_line = slope(bottomPointX, bottomPointY,lastLinePointY, lastLinePointX)
		print('slope_detect_line ',slope_detect_line)
		#slope_centre = 0

		ang = angle(slope_detect_line, 0)
		print("ang ", ang/20)
		pub_angle.publish(ang/20)


	count += 1



if __name__ == '__main__':
	global net, COLORS, pub_angle, pub_speed
	rospy.init_node('video_stream', anonymous=True)
	print('run')
	net, COLORS = load_model_segmentation()

	#khoi tao publisher
	pub_speed = rospy.Publisher('/team1/set_speed', Float32, queue_size=10)  # Khoi tao node speed de phat di
	pub_angle = rospy.Publisher('/team1/set_angle', Float32, queue_size=10)  # Khoi tao node angle de phat di
	rate = rospy.Rate(5)

	#pub_speed.publish(speed)
	#pub_angle.publish(0)
	#subscriber
	image_sub_rgb = rospy.Subscriber('team1/camera/rgb/compressed', CompressedImage, callback_rgb)
	rospy.spin()
