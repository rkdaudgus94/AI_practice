import numpy as np
import cv2

image = cv2.imread('image/mokoko.jpg')
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

green_low = np.array([40,0,0])
green_high = np.array([80,255,255])

my_mask = cv2.inRange(image_hsv, green_low, green_high)

extracted = cv2.bitwise_and(image, image, mask= my_mask)
cv2.imshow('original', image) # 원본
cv2.imshow('mask', my_mask) # 흰색만 추출
cv2.imshow('extracted', extracted) # 특정색만 추출

cv2.waitKey(0)
cv2.destroyAllWindows()