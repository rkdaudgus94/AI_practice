from turtle import back
import numpy as np
import cv2

img1 = cv2.imread('image/mokoko.jpg')
img2 = cv2.imread('image/background.jpg')

front_image = cv2.resize(img1, (300, 400))
back_image = cv2.resize(img2, (300, 400))

img_hsv = cv2.cvtColor(front_image, cv2.COLOR_BGR2HSV)
l_bound = np.array([0,0,0])
u_bound = np.array([0,0,255])

my_mask = cv2.inRange(img_hsv, l_bound, u_bound)
mask_inv = cv2.bitwise_not(my_mask) # 특정색 아닌 픽셀 찾기

extracted = cv2.bitwise_and(front_image, front_image, mask = my_mask) # 특정색 픽셀들만 추출하기
removed = cv2.bitwise_and(front_image, front_image, mask = mask_inv) # 특정색 아닌 픽셀들만 추출하기
background = cv2.bitwise_and(back_image, back_image, mask = my_mask) #  겹치는 배경 추출
merged = cv2.bitwise_or(removed, background) # 특정색 제거 전경 + 배경 추출

cv2.imshow('mask', my_mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('removed', removed)
cv2.imshow('background', background)
cv2.imshow('merged', merged)

cv2.waitKey(0)
cv2.destroyAllWindows()