import cv2

image = cv2.imread('/home/pi/opencv/opencv-master/samples/data/smarties.png', -1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (9, 9), 0)

edged = cv2.Canny(gray, 20, 40)
contours, hierarchy = cv2.findContours(
        edged,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)

out = image.copy()
out.fill(0)
cv2.drawContours(out, contours, -1, (0, 255, 255), 2)
image = cv2.hconcat([image, out])
cv2.imshow('frame', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
