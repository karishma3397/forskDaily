# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:15:43 2018

@author: KC
"""

'''
Consumer Key (API Key)	8PCpsYopUpwLovotBC2dduTRQ
Consumer Secret (API Secret)	BXYWhOPVzN9kJscSMFy0JKY86rYGneXB8TyM38pAGq7iq9onhq
Access Token	2491698797-plmnGcmj39ammb9ttNLleQLo6JUf4GYcJaPfHik
Access Token Secret	V9jdpuyoa8sffYowWf02XJZQYKM39cddx6jkgVsPtgxrS
'''
import twitter
api = twitter.Api(consumer_key='8PCpsYopUpwLovotBC2dduTRQ',
                      consumer_secret='BXYWhOPVzN9kJscSMFy0JKY86rYGneXB8TyM38pAGq7iq9onhq',
                      access_token_key='2491698797-plmnGcmj39ammb9ttNLleQLo6JUf4GYcJaPfHik',
                      access_token_secret='V9jdpuyoa8sffYowWf02XJZQYKM39cddx6jkgVsPtgxrS')
status = api.PostUpdate('I love python-twitter!')

