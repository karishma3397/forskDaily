# -*- coding: utf-8 -*-
"""
Created on Wed May 23 13:05:28 2018

@author: KC
"""

#api key :vZahFUamwp8N06b6Yuwz78SIl-QeQfhu
import requests
api_key = "avBJ-wURMMgF8qAuYFoNsMsWxQQzK8lr"
url = "https://api.mlab.com/api/1/databases/db_students/collections/Students?apiKey="+api_key
data = {"'Student Name": 'karishma', 'Student Age': '21', 'Student Branch': 'cse', 'Student Roll No': '2018'}
r = requests.post(url, json = data )

print(r.text)