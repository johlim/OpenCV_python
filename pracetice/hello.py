import cv2
import sys
import writer_module as mymodule

#cap = cv2. VideoCapture('http://10.138.67.176:4747/video')
cap = cv2. VideoCapture(0)

frame_size=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#writer = mymodule.mp4_writer('./record0.mp4',frame_size)
print('frame zie=', frame_size)

while True:
    retval, frame = cap.read()
    if not retval:
        break
    cv2.imshow('frame', frame)
    print (sys.getsizeof(frame))
#    writer.write(frame)
    key = cv2.waitKey(25)
    if key==27:
        break
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()