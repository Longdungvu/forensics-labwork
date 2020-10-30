import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime


img = cv2.imread('forme3.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("forme1.png", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread("house8.png", cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread("femme.png", cv2.IMREAD_GRAYSCALE)

# change the name of the phto you want to plot
# plt.hist(img4.ravel(),256,[0,256]);
# plt.show()

ret,thresh1 = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img2,120,255,cv2.THRESH_BINARY)
ret,thresh3 = cv2.threshold(img3,60,255,cv2.THRESH_BINARY)
ret,thresh4 = cv2.threshold(img4,100,255,cv2.THRESH_BINARY)



cv2.imshow("image1",thresh1)
cv2.imshow("image2",thresh2)
cv2.imshow("image3",thresh3)
cv2.imshow("image4",thresh4)

cv2.waitKey(0)


# Observe:
# The result from the threshold method can only capture half of the object in forme3.png
# because the intensity of the object is different



# Conclude:
# the histogram method work with the previous photos because the whole object
# we vant to capture located insde a specific intensity range but in case of forme3.png
# the object is located in 2 different intensity threshold so we cant capture it


# Conclusion:
# the histogram method work best when the object you want to seperate is located inside an intensity range
