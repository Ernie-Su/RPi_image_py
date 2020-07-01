import cv2
import numpy as np

src = cv2.imread('/home/pi/opencv/opencv-master/samples/data/smarties.png', -1)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)

circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT, #only supports this argument
        1, #1 means the detect image and input image's size are the same
        10, #the minimum distance between centers of circles
        None, #it's just None
        1, #the upper threshold value of canny, half of it would be lower thre
        75, #a circle can be detected over this threshold value
        3, #the minimum radius of the circle
        75, #the maximum radius of the circle
)

#draw the circles detected
if len(circles)>0:
    out = src.copy()
    for x, y, r in circles[0]:
        cv2.circle(out, (x, y), int(r), (0, 0, 255), 3, cv2.LINE_AA)
        cv2.circle(out, (x, y), 2, (0, 255, 0), 3, cv2.LINE_AA)
    src = cv2.hconcat([src, out])

#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', src)
cv2.waitKey(0)
cv2.destroyAllWindows()

