import cv2

cap = cv2.VideoCapture('/home/pi/opencv/opencv-master/samples/data/vtest.avi')

bg = None

while True:
    ret, frame = cap.read()
    
    #turn it to gray and filter the noise by gaussain blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (17, 17), 0)

    #set the first frame as the background
    if bg is None:
        bg = gray
        continue

    #use bg and gray to do absdiff(), which means minus, and get the differnece
    #use threshold() to do the binariztion, and get only white and black image 
    diff = cv2.absdiff(gray, bg)
    diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]
    
    #do erode(to filter little noises) and dilate(to connect separated images)
    #erode and dilate are opposite process
    #erode() shrinks 3 pixels in white area, while dilate() broaden 3 in black
    #iteration is the times to do of the same function
    diff = cv2.erode(diff, None, iterations=2)
    diff = cv2.dilate(diff, None, iterations=2)

    #findContours() can find the contour between white and black areas
    #RETR_EXTERNAL gets the most external contour
    #CHAIN_APPROX_SIMPLE gets simplified info, e.g. four vertexes in rect
    cnts, hierarchy = cv2.findContours(
            diff,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)

    #cnts is the number of the contours
    #areas calculated by contourArea()<500 can be ignored as noises
    #boundingRect() can draw the smallest rectangle
    for c in cnts:
        if cv2.contourArea(c)<500:
            continue
        
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow('frame', frame)
    cv2.imshow('diff', diff)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break

