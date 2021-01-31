import cv2
import numpy as np

drip = cv2.imread("C:/Users/Raymond/Downloads/drip.png")
face = cv2.imread("C:/Users/Raymond/Downloads/face.jpg") 


scale_percent = 80
width = int(drip.shape[1] * scale_percent / 100)
height = int(drip.shape[0] * scale_percent / 100)
dim = (width, height)

drip = cv2.resize(drip, dim, interpolation = cv2.INTER_AREA)

x_offset = 150
y_offset = 300
face[y_offset:y_offset + drip.shape[0], x_offset:x_offset + drip.shape[1]] = drip

cv2.imshow('drip',face)
cv2.waitKey(0)
cv2.destroyAllWindows