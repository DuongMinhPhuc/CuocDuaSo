import cv2
import numpy as np
#autho tong minh duc
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import os

# image_path = 'images_segmented/5.jpg'
#
# image = cv2.imread(image_path)

def detect_line(image):
    img = image
    img[img[:, :, 0] > 100] = np.array([255, 255, 255])
    img[img[:, :, 0] < 100] = np.array([0, 0, 0])

    x, y = [], []

    #thay range de thay height cua anh
    # 512 * 1024
    #thay 80 bang so lon hon, xoa x[i+5 ben control]
    for index in range(100, img.shape[0], 5):
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

    return y_poly_pred_1.reshape(-1), x.reshape(-1)


# list_y, list_x = detect_line(image)
#
# plt.figure()
# plt.imshow(image)
# plt.plot(list_y, list_x, '-r')
# plt.show()




