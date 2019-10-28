import cv2

image = cv2.imread("gray.jpg",0)
cv2.namedWindow("Image")
print(image.shape)
cv2.imshow("Image", image)
cv2.waitKey(0)