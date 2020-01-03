import cv2
import numpy as np

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

img = cv2.imread('images_segmented/17.jpg')
img[img[:, :, 0] > 100] = np.array([255, 255, 255])
img[img[:, :, 0] < 100] = np.array([0, 0, 0])

x, y = [], []

for index in range(0, img.shape[0], 5):
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

print("y_poly_pred_1.reshape(-1):")
print(y_poly_pred_1.reshape(-1))
print("x.reshape(-1)")
print(x.reshape(-1))

plt.imshow(img)
plt.plot(y, x, 'ob')
plt.plot(y_poly_pred_1.reshape(-1), x.reshape(-1), '-r')
plt.show()
