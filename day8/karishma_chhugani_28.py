# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:20:20 2018

@author: KC
"""
lst = []
#karishma01chhugani@gmail.com
while True:
    str1 = input()
    if not str1:
        break
    if str1.count('@')==1 and str1.count('.')==1:
        str2 = str1.split('@')
        str3=str2[1].split('.')
        if len(str3)==2:
            
    
            import string  
            chk_s = string.ascii_lowercase
            chk_d = '0123456789'
            
            if all(i in chk_s+chk_d+"_-" for i in str2[0]):
                if all(i in chk_s+chk_d for i in str3[0]):
                    if len(str3[1])<3:
                        lst.append(str1)
print(lst)