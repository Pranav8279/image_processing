# import your opencv module
import cv2
# to capture video and access camera
cam = cv2.VideoCapture(0)
# reading and displaying the frames in camera
while True:
    _,frame=cam.read()
    cv2.imshow('webcam',frame)
    # wait for 1ms and check for pressed key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# close the camera
cam.release()
# close the all windows 
cv2.destroyAllWindows()