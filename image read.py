# import a opencv module 
import cv2
# direct your image path to path attribute
path = " #your image path should me written here. "
# read the image using imread function
img = cv2.imread(path)
# display the image using imshow function
cv2.imshow('image', img)
#to break the loop in specified time
cv2.waitKey(0)
# close all windows
cv2.destroyAllWindows()
