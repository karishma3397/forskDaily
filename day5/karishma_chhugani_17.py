# -*- coding: utf-8 -*-
"""
Created on Wed May 16 12:25:27 2018

@author: KC
"""

from PIL import Image
img=input("Enter name of image")
img_filename = Image.open(img)
conv=img_filename.convert('L')
rot=conv.rotate(-90)
crop = rot.crop((rot.size[0]/2-80,rot.size[1]/2-102,rot.size[0]/2+80,rot.size[0]/2+102))
crop.thumbnail((75,75))
crop.save("output.jpg")
print("output.jpg")


