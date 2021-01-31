import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("C:/Users/Raymond/Downloads/haarcascade_frontalface_default.xml")
img = cv2.imread("C:/Users/Raymond/Downloads/gracist.png")

faces = face_cascade.detectMultiScale(img, 1.1, 4)

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

drip = cv2.imread("C:/Users/Raymond/Downloads/dripjacket.png",-1)
face = cv2.imread("C:/Users/Raymond/Downloads/gracist.png") 

cv2.imshow("cropped", img)
cv2.waitKey(0)

width, height = drip.shape[:2]
width2, height2 = img.shape[:2]

# scale = int(3*c/width)
# width = int(drip.shape[1] * scale / 100)
# height = int(drip.shape[0] * scale / 100)
# dim = (width, height)
# drip = cv2.resize(drip, dim, interpolation = cv2.INTER_AREA)
# wscaled, hscaled = drip.shape[:2]

def overlay_transparent(background, overlay, x, y):
    background_width = background.shape[1]
    background_height = background.shape[0]

    if x >= background_width or y >= background_height:
        return background

    h, w = overlay.shape[0], overlay.shape[1]

    if x + w > background_width:
        w = background_width - x
        overlay = overlay[:, :w]

    if y + h > background_height:
        h = background_height - y
        overlay = overlay[:h]

    if overlay.shape[2] < 4:
        overlay = np.concatenate(
            [
                overlay,
                np.ones((overlay.shape[0], overlay.shape[1], 1), dtype=overlay.dtype) * 255
            ],
            axis=2,
        )

    overlay_image = overlay[..., :3]
    mask = overlay[..., 3:] / 255.0
 
    background[y:y + h, x:x + w] = (1.0 - mask) * background[y:y + h, x:x + w] + mask * overlay_image
    print(overlay.shape[:2])

    return background

#translate jacket and scale based on face position
wscaled = int(3*c)
hscaled = int(width*wscaled/height)
drip = cv2.resize(drip, (wscaled,hscaled),interpolation=cv2.INTER_CUBIC)
x = int(a + (c/2) - (wscaled/2))
y = int(b+d-40)

drip = overlay_transparent(face, drip, x, y)

cv2.imshow('drip',face)
cv2.waitKey(0)
cv2.destroyAllWindows

print(a,b,c,d)

print(width, height)
print(width2,height2)
