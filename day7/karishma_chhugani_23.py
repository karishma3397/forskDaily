# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:42:52 2018

@author: KC
"""


import facebook as fb

# Facebook Graphic Explorer API user Access Token
access_token = "EAACEdEose0cBACxZCojQhnh2v6OnZCg8GtbUYL0x5XDsXo58WYAT8qApIHSewJNgTGLbxLZBmmKSDTdHwXwrTzpdZADeSZByR8hyxhZBX10Giig24MQKSkGm2sNWJ1knKDxsRsNxPZCZBrBjSZCpgkwMSfO2maEUaZAGefZAU3Sk5irI9FVCfdJZCAf2gdT1JKXQoekoDv1pwVRzyAZDZD"

# Message to post as status on Facebook
status = "Hell n"

# Authenticating
graph = fb.GraphAPI(access_token)
post_id = graph.put_wall_post(status)

posted_image_id = graph.put_photo(image = open("sample.jpg","rb"), caption = 'Hello')

