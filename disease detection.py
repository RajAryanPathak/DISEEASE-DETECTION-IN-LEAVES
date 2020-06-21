import cv2
import numpy as np
import copy
import easygui
path= easygui.fileopenbox()
img1 = cv2.imread(path)


zz = copy.copy(img1)
## convert to hsv
hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)

#thresholding
ret, thresh1 = cv2.threshold(s, 20, 255, cv2.THRESH_BINARY) 
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)


#edge detection
l= cv2.Canny(closing,100,150,L2gradient=False)




## mask of green (36,25,25) ~ (86, 255,255)
# mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

## slice the green
imask = mask>0
img = np.zeros_like(img1, np.uint8)

img[imask] = img1[imask]



hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

value = 90

vValue = hsvImg[...,2]
hsvImg[...,2]=np.where((255-vValue)<value,255,vValue+value)

g1=cv2.cvtColor(hsvImg,cv2.COLOR_HSV2RGB)

g1=cv2.cvtColor(g1,cv2.COLOR_RGB2BGR)

hsv1 = cv2.cvtColor(g1, cv2.COLOR_BGR2HSV)

## mask of green (36,25,25) ~ (86, 255,255)
# mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
mask1 = cv2.inRange(hsv1, (36, 25, 25), (70, 255,255))



imask1 = mask1>0
green = img1
green[imask1] = g1[imask1]




b,g,r=cv2.split(green)
gtbgr =cv2.cvtColor(g, cv2.COLOR_GRAY2BGR)


row, column = g.shape
# Create an zeros array to store the sliced image
g12 = np.zeros((row,column),dtype = 'uint8')
 
# Specify the min and max range
min_range = 0
max_range = 120
 
# Loop over the input image and if pixel value lies in desired range set it to 255 otherwise set it to 0.
for i in range(row):
    for j in range(column):
        if g[i,j]>min_range and g[i,j]<max_range:
            g12[i,j] = 0
        elif(g[i,j]>120 and g[i,j]<250):
            g12[i,j] = 200
            
        else:
            g12[i,j] = 255
#taking and of images
neg=cv2.bitwise_not(l)
g12= g12 & neg  

            
            
# Display the image
cv2.imshow('sliced image',g12)
cv2.imshow('ori',zz)



cv2.waitKey(0)
cv2.destroyWindow('asd')