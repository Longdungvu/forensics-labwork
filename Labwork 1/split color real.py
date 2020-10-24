import cv2
import numpy

src =cv2.imread("logo-usth.png")
b,g,r = cv2.split(src)
zeros = numpy.zeros(r.shape, numpy.uint8)
blueRGB = cv2.merge((b,zeros,zeros))
redRGB = cv2.merge((zeros,zeros,r))

cv2.imwrite("redreal.png", redRGB)
cv2.imwrite("bluereal.png", blueRGB)
