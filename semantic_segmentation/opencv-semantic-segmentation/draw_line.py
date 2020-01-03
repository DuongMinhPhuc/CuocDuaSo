import cv2
import numpy as np
#autho tong minh duc
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import os

list_images_path = os.listdir("/home/phucxo/catkin_ws/src/semantic_segmentation/opencv-semantic-segmentation/images_segmented")


def detect_line(image_path):
    img = cv2.imread(image_path)

    img[img[:, :, 0] > 100] = np.array([255, 255, 255])
    img[img[:, :, 0] < 100] = np.array([0, 0, 0])

    x, y = [], []

    #thay range de thay height cua anh
    for index in range(80, img.shape[0], 5):
        temp = []
        for i in range(img.shape[1]):
            if np.array_equal(img[index, i, :], np.array([255, 255, 255])):
                temp.append(i)

        try:
            y.append(temp[len(temp) // 2])
            x.append(index)
        except:
            continue

    x = np.array(x)
    y = np.array(y)

    x = x[:, np.newaxis]
    y = y[:, np.newaxis]

    polynomial_features = PolynomialFeatures(degree=2)
    x_poly = polynomial_features.fit_transform(x)

    # model
    model = LinearRegression()
    model.fit(x_poly, y)
    y_poly_pred = model.predict(x_poly)

    a = model.coef_[0][2]
    b = model.coef_[0][1]
    c = model.intercept_[0]

    y_poly_pred_1 = a * x ** 2 + b * x + c

    print(a)
    print(b)
    print(c)

    # plt.imshow(img)
    # plt.plot(y, x, 'ob')
    # plt.plot(y_poly_pred_1.reshape(-1), x.reshape(-1), '-r')
    # plt.show()
    return y_poly_pred_1.reshape(-1), x.reshape(-1)


for image_path in list_images_path:
    print("image_path ",image_path)
    image_segment = "/home/phucxo/catkin_ws/src/semantic_segmentation/opencv-semantic-segmentation/images_segmented/" + image_path
    list_y, list_x = detect_line(image_segment)
    real_image_path = "/home/phucxo/catkin_ws/src/semantic_segmentation/opencv-semantic-segmentation/images/" + image_path
    showImage = cv2.imread(real_image_path)
    segmentImage = cv2.imread(image_segment)

    plt.figure()
    plt.imshow(showImage)
    plt.plot(list_y, list_x, '-r')
    plt.show()

    plt.figure()
    plt.imshow(segmentImage)
    plt.show()




# plt.figure()
# plt.imshow(line_image)
# plt.show()
#read image trang den da duoc segment road



# plt.figure()
# plt.imshow()
# plt.show()

