import cv2

img = cv2.imread("cadastre1.png", cv2.IMREAD_GRAYSCALE)
ret,thresh1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow("image1",thresh1)
cv2.waitKey(0)
