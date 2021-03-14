import cv2  
img  = cv2.imread(r'Images/image.png',1)  
retval, threshold = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)  
cv2.imshow("Threshold",threshold)
cv2.waitKey(0)  
