# ImageToAscii
Image input, .txt output
This script can be used in two ways. Run as-is, or imported into another file.
The output either way is simply 20 strings of ASCII art. the first is a 1:1 of the source image, and the 20th is 1/20th of the soure.

> Run as-is
>> When run it will ask the user for an image and a directory to save the output text files into.


> imported into another file
>> When imported and given a raster image and a Light/Dark Mode setting it will output a list containing 20 strings


Example Code:

```py
import ImageToAscii as I2A
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os


def GetAsciiList():
    Window = tk.Tk()
    Window.withdraw()
    print('Please select an image.')
    ImageChoice = filedialog.askopenfilename(
        initialdir=os.path.dirname(os.path.abspath(__file__)),
        title='Select Image',
        filetypes=[("Image Files",".jpg .png .jpeg .bpg .tif")])

    DarkList = I2A.ImageToAscii(Image.open(ImageChoice), Mode='Dark').FullList()
    for each in DarkList:
        print(each)
    LightList = I2A.ImageToAscii(Image.open(ImageChoice), Mode='Light').FullList()
    for each in LightList:
        print(each)


GetAsciiList()
```
From:

![Oh?!](https://raw.githubusercontent.com/CaptiosusNomen/ImageToAscii/master/Images/WALK.jpg)



Into:
![Dark Mode](https://raw.githubusercontent.com/CaptiosusNomen/ImageToAscii/master/AsciiArt/DarkMode3.png)

![Light Mode](https://raw.githubusercontent.com/CaptiosusNomen/ImageToAscii/master/AsciiArt/LightMode3.png)




