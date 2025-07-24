from PIL import Image
import cv2
import numpy as np

image_path ='image.jpg'
image = cv2.imread(image_path)

resized_image = cv2.resize(image,(300,300))
cv2.imshow('resize image',resized_image)

blurred_image = cv2.GaussianBlur(resized_image,(5,5),0)
cv2.imshow('Blurred Image',blurred_image)

gray_image = cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)
ret,thresholded_image = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)
cv2.imshow('threshold image',thresholded_image)


cv2.waitKey(0)

cv2.destroyAllWindows()
