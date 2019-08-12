import cv2

img = cv2.imread('guitar.jpg', 0)

limiar, imgLimiar = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
limiar, imgLimiar1 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)
limiar, imgLimiar2 = cv2.threshold(img, 150, 255, cv2.THRESH_TRUNC)

cv2.imshow('Limiar Binary', imgLimiar)
cv2.imshow('Limiar Binary INV', imgLimiar1)
cv2.imshow('Limiar Trunc', imgLimiar2)


cv2.waitKey(0)
cv2.destroyAllWindows()

