import PySimpleGUI as sg
import os
from PIL import Image, ImageTk
import io
import subprocess

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
    newLayout = [
        [sg.Image(data=get_img_data(path, first=True))],
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
        createDrip()
        window.close()
        break
    if event == "Cancel" or event == sg.WIN_CLOSED:
        window.close()
        break


