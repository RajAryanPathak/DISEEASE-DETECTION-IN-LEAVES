#importing libraries
import cv2
import easygui
import copy
import  numpy as np



def Sort_Tuple(tup):  
    return(sorted(tup, key = lambda x: x[1]))  


#taking image and converting it into hsv and splitting it
path= easygui.fileopenbox()
img = cv2.imread(path)
hsv =cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)

#thresholding
ret, thresh1 = cv2.threshold(s, 20, 255, cv2.THRESH_BINARY) 
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)


#edge detection
l= cv2.Canny(closing,100,150,L2gradient=False)


#mathematical calculation
a = np.asarray(img)
s=[]
indices = np.where(l == [255])#take all the value which are equal to 255
a = [(indices[0][i], indices[1][i]) for i in range(0, len(indices[0]))] #store them as x and y coordinate


#sorting the tuple
a=Sort_Tuple(a) #sort them acc. to second value


#keeping the left  most values in a list
m=[]
t=a[0]
t1=a[0][1]
m.append(t)
for i in range(1,len(a)):
    if(a[i][1]==t1):
        continue        
    else:
        t=a[i]
        t1=a[i][1]
        m.append(t)
        
        
#finding the average of points on a scale of 10       
s = [(m[i][0]) for i in range(0, len(m))] 
len1=len(s)
factor=len(s)//10
avg=[]
for i in range(0,len(s)-factor,factor):
    te=(round((s[i]+s[i+1]+s[i+2])/factor,2))
    avg.append(te)
print(avg)


#finding the pattern of the points
for i in range(len(avg)):
    if(avg[i]>avg[i+1]):
        continue
    else:
        k=avg[i]
        break
        
if(k==min(avg)):
    print("yes")


else:
    print("no")


#displaying image
cv2.imshow('boundary ', l)
cv2.waitKey(0)
cv2.destroyAllWindows()

