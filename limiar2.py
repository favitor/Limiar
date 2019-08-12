import cv2
import numpy as np 

img = cv2.imread('coins.jpg', 0)

adp = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
							cv2.THRESH_BINARY, 11, 2)
adp2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
							cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Original', img)
cv2.imshow('Mean', adp)
cv2.imshow('Gaussian', adp2)

cv2.waitKey(0)
cv2.destroyAllWindows()
