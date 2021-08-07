import cv2
import numpy as np
import os


class basicColor:
    def __init__(self, path):
        imagen = cv2.imread(path)               # read image
        self.img = imagen                       # store image in self as img
        
    def displayProperties(self):
        pixels = self.img.shape[0] * self.img.shape[1]      # calculate number of pixels from dimensions
        canales = self.img.shape[2]                         # extract number of channels
        print('Number of pixels is: {}'.format(pixels))
        print('Number of channels is: {}'.format(canales))
        
    def makeBW(self):                           # OTSU global treshold
        img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)   # transform space color
        ret, Ibw_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # finding ibw value
        cv2.imshow("Image", Ibw_otsu)                           # plotting output image
        cv2.waitKey(0)
    
    def colorize(self,h):                   # Colorise image from h input value
        img_hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)     # transform space color from BGR to HSV
        img_hsv[:,:,0] = h                  # assign h value to Hue pixels
        img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)      # transform space color back to BGR from HSV
        cv2.imshow("Image", img_bgr)
        cv2.waitKey(0)
       
        
# Get image path from user 
print("Insert path image") 
path = input() # C:/Users/User/Pictures/salto.jpg
print()

# Display properties
temp = basicColor(path)
temp.displayProperties()
print()

# OTSU equalization
temp.makeBW()
print()

# Colorise image from h input
print("Insert h value")
h = input()
temp.colorize(h)
