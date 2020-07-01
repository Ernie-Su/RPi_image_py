import cv2
import numpy as np

gc = np.zeros((512, 512, 3), dtype=np.uint8)
gc[:] = [48, 213, 254]

cv2.line(gc, (10, 50), (400, 300), (255, 0, 0), 5)
cv2.rectangle(gc, (10, 50), (400, 300), (0, 0, 255), 5)
cv2.rectangle(gc, (100, 200), (396, 296), (234, 151, 102), -1)
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(gc, 'JoJo', (10, 200), font, 4, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('draw', gc)

cv2.waitKey(0)
cv2.destroyAllWindows()
