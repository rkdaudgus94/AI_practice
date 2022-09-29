import cv2
global color_image, gray_image

def on_change_threshold(x) :
    _, th_image = cv2.threshold(gray_image, x, 255, cv2.THRESH_BINARY)
    cv2.imshow('Thresholding', th_image)


cv2.namedWindow('Thresholding')
cv2.createTrackbar('threshold', 'Thresholding', 0, 255, on_change_threshold)

color_image = cv2.imread('image/mokoko.jpg', cv2.IMREAD_COLOR)
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Thresholding', color_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

