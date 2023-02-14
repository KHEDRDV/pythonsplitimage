import cv2 
 
# Read the image 
img = cv2.imread('input.jpeg') 
 
# Split the image into two halves 
width = img.shape[1] // 2
first_half = img[:, :width] 
second_half = img[:, width:] 
 
# Save the two halves 
cv2.imwrite('first_half.jpg', first_half) 
cv2.imwrite('second_half.jpg', second_half)