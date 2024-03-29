import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import time

#reads the template image and the image being searched through as greyscale
img = cv2.imread('D_2.png', 0)

img2 = img.copy()
#template = cv2.imread('D_Temp.png',0)
original = cv2.imread('D_Temp.png',0)
ret,template = cv2.threshold(original, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('image', template)


w, h = template.shape[::-1]

#compares the two images using a certain algo we chose
res = cv2.matchTemplate(img,template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
#create rectangle around the detected match
cv2.rectangle(img,top_left, bottom_right, 255, 2)
#show it to user
plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle('TM_CCOEFF')

#show the compared images
plt.show()
print(max_val)




