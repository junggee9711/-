import cv2
import numpy as np
from functions import reverse, gradation

iHeight = 256
iWidth = 256

image = cv2.imread('Lena.jpg')

# for visualization (opens a new window)
cv2.imshow('Lena', image)
cv2.waitKey(0)

img_reversed, img_reversed2 = reverse(image, iHeight, iWidth)
cv2.imshow('Lena_reversed', img_reversed)
cv2.imshow('Lena_reversed2', img_reversed2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Lena_reversed.jpg', img_reversed)

img_gradation_vertical, img_gradation_horizontal = gradation(iHeight, iWidth)
cv2.imshow('gradation_vertical', img_gradation_vertical)
cv2.imshow('gradation_horizontal', img_gradation_horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('gradation_vertical.jpg', img_gradation_vertical)
cv2.imwrite('gradation_horizontal.jpg', img_gradation_horizontal)