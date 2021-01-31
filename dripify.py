import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("C:/Users/Raymond/Downloads/haarcascade_frontalface_default.xml")
img = cv2.imread("C:/Users/Raymond/Downloads/face.jpg")

# detect faces
faces = face_cascade.detectMultiScale(img, 1.1, 4)
# draws rectangle around detected faces

area = 0
a = 0
b = 0
c = 0
d = 0

for (x, y, w, h) in faces:
    if area < (x + w) * (y + h):
        area = (x + w) * (y + h)
        a = x
        b = y
        c = w
        d = h


cv2.rectangle(img, (a, b), (a + c, b + d), (255, 0, 0), 2)
    # crop_img = img[y:y + h, x:x + w]

drip = cv2.imread("C:/Users/Raymond/Downloads/drip.png")
face = cv2.imread("C:/Users/Raymond/Downloads/face.jpg") 

#scale jacket
scale_percent = 80
width = int(drip.shape[1] * scale_percent / 100)
height = int(drip.shape[0] * scale_percent / 100)
dim = (width, height)

drip = cv2.resize(drip, dim, interpolation = cv2.INTER_AREA)

#scale face


x_offset = 100
y_offset = 100
face[y_offset:y_offset + drip.shape[0], x_offset:x_offset + drip.shape[1]] = drip

cv2.imshow('drip',face)
cv2.waitKey(0)
cv2.destroyAllWindows
