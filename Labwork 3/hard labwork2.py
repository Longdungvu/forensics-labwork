import cv2
import numpy as np

img = cv2.imread("cadastre2.png", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5,5),np.uint8)

for _ in range(3):
    img = cv2.GaussianBlur(img, (5, 5), 0)

thresh1 = cv2.inRange(img, 60, 110)
opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel, iterations=2)
# cv2.imshow("image1",thresh1)

result = thresh1 - opening

a = result2
cv2.imshow("image1", cv2.resize(a, (a.shape[1]//2, a.shape[0]//2)))
cv2.waitKey(0)
