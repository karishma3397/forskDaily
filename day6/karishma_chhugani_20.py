# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:26:48 2018

@author: KC
"""

import requests
API_Endpoint = "http://13.127.155.43/api_v0.1/sending"

data = {'Phone_Number' : '9039170360',
        'Name' : 'Karishma',
        'College_Name':'SATI',
        'Branch':'CSE'}
r = requests.post(url = API_Endpoint, json = data)
print (r.text)
url = "http://13.127.155.43/api_v0.1/receiving"
url+='?Phone_Number=9039170360'
response = requests.get(url)
print(response.text)