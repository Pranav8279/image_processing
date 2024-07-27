# import your opencv module
import cv2
# import your numpy module 
import numpy as np
#define a function to change the size of image
def resize_image(image,size):
    return cv2.resize(image,size,interpolation=cv2.INTER_AREA)
# direct your image path to path attribute
path1 = " # your image path should be written here. "
path2= " # your image path should be written here. "
# read the image using imread function
image1 = cv2.imread(path1)
image2= cv2.imread(path2)
# call the function to resize the image
resize_dim=(200,200)
# now resize your images
image1=resize_image(image1,resize_dim)
image2=resize_image(image2,resize_dim)
# display the resized images
top_row=np.hstack((image1))
bottom_row=np.hstack((image2))
collage=np.vstack((top_row,bottom_row))
cv2.imshow("output",collage)
#to break the loop in specified time
cv2.waitKey(0)
# to destroy or to stop the code
cv2.destroyAllWindows()