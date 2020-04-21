# Reference :https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
import numpy as np 
import cv2
cap =cv2.VideoCapture(-1,cv2.CAP_V4L)
while(True):
    ret, frame = cap.read()
    if ret:
        pass
    else:
        print "Problem loading"
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
if ret:
    cap.release()
    cv2.destroyAllWindows()
else:
    pass