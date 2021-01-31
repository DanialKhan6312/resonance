import PySimpleGUI as sg
import os

import cv2
from PIL import Image, ImageTk
import io
import subprocess

import dripify

def get_img_data(f, maxsize=(1200, 850), first=False):
    """Generate image data using PIL
    """
    print(f)
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)

def createDrip():
    # print(path)

    # print(type(path))

    drip = dripify.drippify(path)
    cv2.imwrite('dripppyyy.jpg', drip)

    newLayout = [
        [sg.Image(data=get_img_data('dripppyyy.jpg', first=True))],
        [sg.Submit("DRIPPY!")]
    ]
    newWindow = sg.Window('Dripify', newLayout, size=(1200, 850))
    while True:
        event, values = newWindow.read()
        # End program if user closes window or
        # presses the OK button
        if event == "DRIPPY!" or event == sg.WIN_CLOSED:
            window.close()
            break


path = sg.popup_get_file('Image to open', default_path='')

layout = [
     [sg.Submit("Get drip"), sg.Cancel("Cancel")]
]
window = sg.Window('Dripify', layout, size=(300, 100))
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Get drip":
        window.close()
        createDrip()
        break
    if event == "Cancel" or event == sg.WIN_CLOSED:
        window.close()
        break


