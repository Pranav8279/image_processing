# import opencv modules
import cv2
# to capture video and access camera
cam=cv2.VideoCapture(0)
# getting information 
width=cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps=cam.get(cv2.CAP_PROP_FPS)
# reading and displaying frames in camera
while True:
    i,frame=cam.read()
    cv2.imshow('Webcam',frame)
    print('resolution:',width,'x',height,'|frames per second:',fps)
    # wait for 1ms and check for pressed key
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
#close the camera
cam.release()
#destroy all opened windows
cv2.destroyAllWindows()

              

            
            