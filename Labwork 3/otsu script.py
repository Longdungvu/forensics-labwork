import cv2
import numpy

# Using OTSU's method, we can achieve a high seperable images, without
# during it manually, the method of which results in possible high error
# due to the incorrectness of human nature.

# However, this method is not 100% correct all the time, as seen in the
# exapmple of forme3.png, the example in which we have a T letter being
# shined on by a gradient light. This makes the thresholding becomes hard
# and produce incorrect seperation.

img = cv2.imread("forme1.png", cv2.IMREAD_GRAYSCALE)
# img2 = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread("forme3.png", cv2.IMREAD_GRAYSCALE)

ret,thresh1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# ret,thresh2 = cv2.threshold(img2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret,thresh3 = cv2.threshold(img3,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("image1",thresh1)
# cv2.imshow("image2",thresh2)
cv2.imshow("image3",thresh3)
cv2.waitKey(0)


#
