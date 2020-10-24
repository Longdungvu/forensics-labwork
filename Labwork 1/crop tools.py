import cv2

image = cv2.imread("football.jpeg")


croppped = image[74:230,247:333]
cv2.imshow("cropped", croppped)
k = cv2.waitKey(0)
if k == ord("s"):
    cv2.imwrite("red_player_cropped.png", croppped)
