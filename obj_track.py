import cv2
cap = cv2.VideoCapture('/home/pi/opencv/opencv-master/samples/data/vtest.avi')

#Use CSRT algorithm to track
tracker = cv2.TrackerCSRT_create()
roi = None

while True:
    ret, frame = cap.read()
    
    #selectROI waits user use mouse to select a rectangle
    #after a rect selected, press space to continue
    #to cancel, press c and selectROI returns (0, 0, 0, 0)
    if roi is None:
        roi = cv2.selectROI('frame', frame)
        if roi != (0, 0, 0, 0):
            tracker.init(frame, roi)

    success, rect = tracker.update(frame)
    if success:
        (x, y, w, h) = [int(i) for i in rect]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break
