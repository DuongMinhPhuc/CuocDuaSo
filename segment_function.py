# USAGE
# python segment.py --model enet-cityscapes/enet-model.net --classes enet-cityscapes/enet-classes.txt --colors enet-cityscapes/enet-colors.txt --image images/example_01.png
# python segment.py --image images/10.jpg
# import the necessary packages
import numpy as np
import argparse
import imutils
import time
import cv2


def load_model_segmentation():
    CLASSES = open('enet-cityscapes/enet-classes.txt').read().strip().split("\n")
    COLORS = open('enet-cityscapes/enet-color-black.txt').read().strip().split("\n")
    COLORS = [np.array(c.split(",")).astype("int") for c in COLORS]
    COLORS = np.array(COLORS, dtype="uint8")

    legend = np.zeros(((len(CLASSES) * 25) + 25, 300, 3), dtype="uint8")

    for (i, (className, color)) in enumerate(zip(CLASSES, COLORS)):
        color = [int(c) for c in color]
        cv2.putText(legend, className, (5, (i * 25) + 17),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.rectangle(legend, (100, (i * 25)), (300, (i * 25) + 25),
                      tuple(color), -1)

    print("[INFO] loading model...")
    net = cv2.dnn.readNet('enet-cityscapes/enet-model.net')
    return net, COLORS


def segment_image(input_image, net, COLORS):
    image = imutils.resize(input_image, width=320)
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (1024, 512), 0,
                                 swapRB=True, crop=False)
    net.setInput(blob)
    start = time.time()
    output = net.forward()
    end = time.time()

    print("[INFO] inference took {:.4f} seconds".format(end - start))
    (numClasses, height, width) = output.shape[1:4]
    print("(numClasses, height, width) = output.shape[1:4]")
    print(output.shape[1:4])
    classMap = np.argmax(output[0], axis=0)
    print("output[0]")
    print(output[0])
    mask = COLORS[classMap]

    mask = cv2.resize(mask, (image.shape[1], image.shape[0]),
                      interpolation=cv2.INTER_NEAREST)

    output = (1 * mask).astype("uint8")

    return output



net, COLORS = load_model_segmentation()

image = cv2.imread('images/10.jpg')
output = segment_image(image, net, COLORS)

# cv2.imshow("Legend", legend)
cv2.imshow("Input", image)
cv2.imshow("Output", output)
cv2.waitKey(0)