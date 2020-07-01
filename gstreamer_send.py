import time
import cv2

model = cv2.face.LBPHFaceRecognizer_create()
model.read('faces.data')
print('load training data done')

face_cascade = cv2.CascadeClassifier('/home/pi/opencv/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

WIDTH = 640
HEIGHT = 480
fps = 30

#recognizable name
names = ['Ernie']

#cap = cv2.VideoCapture('videotestsrc ! video/x-raw, width=640, height=480, framerate=30/1 ! appsink', cv2.CAP_GSTREAMER)

#fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#out = cv2.VideoWriter('appsrc ! videoconvert ! x264enc ! rtph264pay ! udpsink host=192.168.0.13 port=5000', cv2.CAP_GSTREAMER, 0, fps, (WIDTH, HEIGHT), True)
out = cv2.VideoWriter('appsrc ! queue ! videoconvert ! video/x-raw ! omxh264enc ! video/x-h264 ! h264parse ! rtph264pay ! udpsink host=192.168.0.13 port=5000', cv2.CAP_GSTREAMER, 0, fps, (WIDTH, HEIGHT), True)
#out = cv2.VideoWriter('appsrc ! videoconvert ! omxh264enc ! rtph264pay ! udpsink host=192.168.0.13 port=5000', cv2.CAP_GSTREAMER, 0, fps, (WIDTH, HEIGHT), True)

if not cap.isOpened() or not out.isOpened():
    print('VideoCapture() or VideoWriter is not opened, exiting')
    exit(0)

#out = cv2.VideoWriter(gst_str_rtp, 0, fps, (WIDTH, HEIGHT), True)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.flip(frame, 0)
    
    if not ret:
        print('empty frame')
        break
    
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 2, 5)
    #reconize faces and match it with traing model
    for(x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        face_image = cv2.resize(gray[y:y+h, x:x+w], (600, 600))
        
        try:
            val = model.predict(face_image)
            print('label:{}, confidence:{}'.format(val[0], val[1]))
            
            #LBPH faith values are better for lower than 50, lower is better
            if val[1]<50:
                cv2.putText(
                    frame, names[val[0]], (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (255, 255, 0), 3, cv2.LINE_AA
                )
        except:
            continue
    
    out.write(frame)
    cv2.imshow('send', frame)
    
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        out.release()
        break
