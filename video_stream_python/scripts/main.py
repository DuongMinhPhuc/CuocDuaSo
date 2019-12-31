#! /usr/bin/python

from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import CompressedImage
import rospy
import cv2
import numpy as np


def callback_depth(data):
	print("depth")
	bridge = CvBridge()
	try:
		np_arr = np.fromstring(data.data, np.uint8)
		cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
	except CvBridgeError as e:
		print(e)

	cv2.imshow('depth', cv_image)
	cv2.waitKey(3)

def callback_rgb(data):
	print("rgb")
	bridge = CvBridge()
	try:
		np_arr = np.fromstring(data.data, np.uint8)
		cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
	except CvBridgeError as e:
		print(e)

	cv2.imshow('rgb', cv_image)
	cv2.waitKey(3)

if __name__ == '__main__':
	rospy.init_node('video_stream', anonymous=True)
	print('run')
	# image_sub_depth = rospy.Subscriber('team1/camera/depth/compressed', CompressedImage, callback_depth)
	image_sub_rgb = rospy.Subscriber('team1/camera/rgb/compressed', CompressedImage, callback_rgb)
	rospy.spin()
