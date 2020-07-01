import cv2

cap = cv2.VideoCapture(0)
#ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH)/cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#WIDTH = 600
#HEIGHT = int(WIDTH/ratio)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)


ESC = 27

while(True):
  ret, frame = cap.read()
  frame = cv2.resize(frame, (600, 450))
  #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  frame = cv2.flip(frame, 0)
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  cv2.imshow('Blurred Frame', frame)

  if cv2.waitKey(1) == ESC:
    break

cap.release()

cv2.destroyAllWindows()
