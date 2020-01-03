#! /usr/bin/python

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

net = 0
COLORS = 0
count = 0
count_image = 0
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
	global count, count_image
	global net, COLORS
	print("rgb")
	bridge = CvBridge()
	try:
		np_arr = np.fromstring(data.data, np.uint8)
		cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
	except CvBridgeError as e:
		print(e)

	cv2.imshow('rgb', cv_image)

	#write image
	if count % 20 == 0:
		#write real image
		#cv2.imwrite('data/'+'realImage/'+str(count_image)+'.jpg', np.array(cv_image))
		print("save image" + 'data/'+'realImage/'+str(count_image)+'.jpg')

		#show segmentation image
		pathRealImage = "/home/phucxo/" + 'data/' + 'realImage/' + str(count_image) + '.jpg'
		inputSegmentImage = cv2.imread(pathRealImage)
		segmentImage = segment_image(inputSegmentImage, net, COLORS)

		#cv2.imwrite('data/' + 'segmentImage/' + str(count_image) + '.jpg', np.array(segmentImage))
		cv2.imshow("segmentImage", segmentImage)
		cv2.waitKey(3)

		count_image += 1

	count += 1





if __name__ == '__main__':
	global net, COLORS
	rospy.init_node('video_stream', anonymous=True)
	print('run')
	net, COLORS = load_model_segmentation()
	# image_sub_depth = rospy.Subscriber('team1/camera/depth/compressed', CompressedImage, callback_depth)
	image_sub_rgb = rospy.Subscriber('team1/camera/rgb/compressed', CompressedImage, callback_rgb)
	rospy.spin()
