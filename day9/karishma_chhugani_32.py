# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:09:42 2018

@author: KC
"""

import re
#regex = re.compile(r'^[456][0-9]{3}[0-9]{4}[0-9]{4}[0-9]{4} | ^[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$')
regex = re.compile(r'^[456](\d{15}|\d{3}(-\d{4}){3})')
list1 = []
while True:
    str1 = input()
    if not str1:
        break
    list1.append(str1)
for i in list1:
    response = regex.match(i)
    conti = re.search(r"(\d)\1{4,}",i.replace("-",""))
    if response and not conti:
        print("Valid")
    else:
        print("Invalid")
