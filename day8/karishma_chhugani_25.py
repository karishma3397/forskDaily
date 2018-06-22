# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:07:53 2018

@author: KC
"""
'''
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
[('Tom', 19, 80), ('John', 20, 90), ('Jony', 17, 91), ('Jony', 17,93), ('Json', 21,85)]
'''
list1 = []
while True:
    str1 = input()
    if not str1:
        break
    tup1 = str1.split(',')
    list1.append((tup1[0],int(tup1[1]),int(tup1[2])))
list1.sort()
