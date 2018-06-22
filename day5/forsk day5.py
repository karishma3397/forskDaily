# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:54:55 2018

@author: KC
"""

fp = open("test.txt",'w')
fp.write("Machine learning")
fp.close()
fp = open("test.txt",'r')
print (fp.read())
#%%
import zlib
s = "Python is not a snake. Its a programming language"
len(s)
s=s.encode('utf-8')
t = zlib.compress(s)
#%%
import urllib.request
f=urllib.request.urlopen("http://google.com/")#check
#%%
import os
os.getcwd()
#%%
from PIL import Image
img_filename = Image.open("sample.jpg")
img_filename.show()

from PIL import ImageFilter

img_filename.filter(ImageFilter.BLUR).show()

img_filename.mode