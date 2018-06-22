# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:45:17 2018

@author: KC

"""

def bricks(a,b,c):
    yes = 0
    for i in range(0,a+1):
        for j in range(0,b+1):
            if i+j*5==c:
                yes+=1
    if yes>0:
        print(True)
        
    else:
        print(False)
print("enter a,b and c")
lst = input().split(",")
lst = map(int,lst)
a,b,c = lst

bricks(a,b,c)
 