# DISEEASE-DETECTION-IN-LEAVES
image pre-processing, segmentation, feature extraction, classification. By computing amount of disease present in the leaf, we can use sufficient amount of pesticides to effectively control the pests in turn the crop yield will be increased. 

1.	In this we have first try identify whether the given image has a leave or not. 
a.	This is done by finding the boundary of the object.
b.	Boundary is found by following process.
i.	Image is converted into HSV
ii.	Appropriate thresholding is applied on image and image of target object is identified.
iii.	Noise is removed from obtained image by applying closing and opening.
iv.	Then Boundary of the object is extracted by using canny edge detection
c.	After the boundary is found we extract the coordinated of the boundary by appending the entire coordinate in array from image whose intensity value is 255
d.	After the coordinates are extracted we check the relation between the consecutive values in the array. 
e.	We replace the values of array by average of 10 consecutive values of array. This is done to generalize the array which will help in finding whether it is a leaf or not.
f.	As we have 2 sides of leaves we have maintain 2 arrays.
g.	For the first array (left) if the value in the array keeps increasing and suddenly start decreasing after a certain point. It will satisfy the criteria of leaves
h.	For the Second array (right) if the value in the array keeps decreasing and suddenly starts increasing after a certain point. It will satisfy the criteria of leaves
i.	If both the criteria are satisfied we will classify it as a leaf
2.	Then we find disease in the leaves.
a.	First we apply mask of green colour and extract the leaf from the image by applying a mask of green colour
b.	Then we increase the brightness of extracted green part so there is visible difference between leaves and disease part
c.	Then we paste the increased brightness image into the original image 
d.	Then we do a RGB split on the image and extract the green part from the image.
e.	As we extract the green part difference become much visible between leaf and disease part
f.	Now we apply grey level slicing on the image and disease part gets highlighted and other parts become white
g.	We extract the highlighted part and impose it on original image and thus disease is found.
