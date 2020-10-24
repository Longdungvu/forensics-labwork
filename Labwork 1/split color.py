
import cv2

src =cv2.imread("logo-usth.png")
b,g,r = cv2.split(src)
cv2.imwrite("red.png", r)
cv2.imwrite("blue.png", b)
cv2.imwrite("green.png", g)
