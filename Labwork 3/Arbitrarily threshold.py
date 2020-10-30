import cv2
import numpy

img = cv2.imread("forme1.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("house8.png", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread("femme.png", cv2.IMREAD_GRAYSCALE)
ret,thresh1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img2,100,255,cv2.THRESH_BINARY)
ret,thresh3 = cv2.threshold(img3,100,255,cv2.THRESH_BINARY)

cv2.imshow("image1",thresh1)
cv2.imshow("image2",thresh2)
cv2.imshow("image3",thresh3)
cv2.waitKey(0)

# conclude:
# the result is not very clear because it base on a random chosen number by human without refer to any given data
