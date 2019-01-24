import pyautogui
#import cv2
import numpy as np
import time

##
##sum = [ 0, 0, 0];
##fileName = "1.png";
##pyautogui.screenshot(fileName);
##screenshot = cv2.imread(fileName)
##screenshot = cv2.resize(screenshot, (0,0), fx=0.2, fy=0.2)
##
##arr = np.array(screenshot)
##
##cv2.imshow('tracking',screenshot)
##print ( "x", x );
##print ( "y", y );
##
##print(arr)
##print (screenshot[0][0])
##
##


from sklearn.cluster import KMeans
from collections import Counter
import cv2 #for resizing image

def get_dominant_color(image, k=4, image_processing_size = None):
    """
    takes an image as input
    returns the dominant color of the image as a list
    
    dominant color is found by running k means on the 
    pixels & returning the centroid of the largest cluster

    processing time is sped up by working with a smaller image; 
    this resizing can be done with the image_processing_size param 
    which takes a tuple of image dims as input

    >>> get_dominant_color(my_image, k=4, image_processing_size = (25, 25))
    [56.2423442, 34.0834233, 70.1234123]
    """
    #resize image if new dims provided
    if image_processing_size is not None:
        image = cv2.resize(image, image_processing_size, 
                            interpolation = cv2.INTER_AREA)
    image  = image.reshape((image.shape[0]*image.shape[1]), image.shape[2])       
    #image = np.asarray(image)        
    #reshape the image to be a list of pixels
    #image = image.reshape(image.shape[0] * image.shape[1], 3)
    #arr = np.array(image)
    #print(arr)
    #cluster and assign labels to the pixels 
    clt = KMeans(n_clusters = k)
    labels = clt.fit_predict(image)

    #count labels to find most popular
    label_counts = Counter(labels)

    #subset out most popular centroid
    dominant_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]

    return list(dominant_color)

def create_blank(width, height, rgb_color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image

while (1):
    fileName = "1.png";
    pyautogui.screenshot(fileName);
    screenshot = cv2.imread(fileName)
    screenshot = cv2.resize(screenshot, (0,0), fx=0.2, fy=0.2)
    maxX = len(screenshot[0]);
    maxY = len(screenshot);

    print((maxX, maxY))
    
    x = int(maxX * 0.2)
    y = int(maxY * 0.2)
    h = int(maxY * 0.6)
    w = int(maxX * 0.6)

    print(x,y,h,w)
    crop_img = screenshot[y:y+h, x:x+w]
    screenshot = crop_img
    dominantColor = get_dominant_color(screenshot, k=2 )
    print(dominantColor)
    img = create_blank(maxX,maxY,( int(dominantColor[2]),int(dominantColor[1]),int(dominantColor[0]) ))
    cv2.imshow('DominantColor',img)
    #cv2.imshow('cropScreenshot',crop_img)

    cv2.imshow('screenshot',screenshot)
    key = cv2.waitKey(2) & 0xFF
    if key == ord("q"):
       break
    #time.sleep(10)
    
cv2.destroyAllWindows()     
