import cv2

RECT, HEXAGON = 0, 1
frame = cv2.imread('poly.png')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 50, 150)
edged = cv2.dilate(edged, None, iterations=1)
contours, heirarchy = cv2.findContours(
        edged,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)

print('-----Before Process-----')
print('Rectangle points number : {}'.format(len(contours[RECT])))
print('Hexagon points number : {}'.format(len(contours[HEXAGON])))

#
approx_rect = cv2.approxPolyDP(contours[RECT], 10, True)
approx_hex = cv2.approxPolyDP(contours[HEXAGON], 10, True)

print('-----After Process-----')
print('Rectangle points numer : {}'.format(len(approx_rect)))
print('Hexagon points number : {}'.format(len(approx_hex)))

cv2.drawContours(frame, [approx_rect], -1, (0, 0, 255), 5)
cv2.drawContours(frame, [approx_hex], -1, (0, 0, 255), 5)

cv2.imshow('image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
