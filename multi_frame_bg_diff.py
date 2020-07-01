import cv2

bs = cv2.bgsegm.createBackgroundSubtractorMOG()
cap = cv2.VideoCapture(0)
ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH)/cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
WIDTH = 600
HEIGHT = int(WIDTH/ratio)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.flip(frame, 0)

    #tracker algorithm in opencv automatically do gray scale and gaussian blur
    #so just use apply()
    gray = bs.apply(frame)
    mask = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)[1]
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, hierarchy = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c)<200:
            continue
        
        #draw contours
        cv2.drawContours(frame, contours, -1, (0, 255, 255), 2)
        
        #draw rectangle
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #use hconcat() to combine the formal frame and binarized image and output
    mask = cv2. cvtColor(mask, cv2.COLOR_GRAY2BGR)
    frame = cv2.hconcat([frame, mask])
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break
