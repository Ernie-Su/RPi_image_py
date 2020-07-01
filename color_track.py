import cv2
import numpy as np

wierd = ((0, 0), (599, 39))
(left, top), (right, bottom) = wierd

def wierdarea(frame):
    return frame[top:bottom, left:right]

def replacewierd(frame, wa):
    frame[top:bottom, left:right] = wa
    return frame

color = ((16, 59, 0), (47, 255, 255))
lower = np.array(color[0], dtype="uint8")
upper = np.array(color[1], dtype="uint8")

cap = cv2.VideoCapture(0)
#ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH)/cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#print('ratio = {}'.format(ratio))
#WIDTH = 600
#HEIGHT = int(WIDTH/ratio)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (600, 450))
    frame = cv2.flip(frame, 0)
    
    wa = wierdarea(frame)
    wa = cv2.cvtColor(wa, cv2.COLOR_RGB2BGR)
    frame = replacewierd(frame, wa)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.GaussianBlur(hsv, (11, 11), 0)

    #inRange() can do binarization between lower and upper in hsv
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, hierarchy = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)

    #we assume our target has the biggest contour area rather than the noises
    if len(contours)>0:
        cnt = max(contours, key=cv2.contourArea)
        if cv2.contourArea(cnt)>100:
            x, y, w, h = cv2.boundingRect(cnt)
            x1, y1, x2, y2 = x-2, y-2, x+w+4, y+h+4

            out = cv2.bitwise_and(hsv, hsv, mask=mask)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(hsv, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(out, (x1, y1), (x2, y2), (0, 255, 0), 2)

    frame = cv2.hconcat([frame, hsv, out])
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break
