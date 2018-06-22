# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:55:45 2018

@author: KARIS
"""

#api key : e5504afb-4929-4b48-bf64-e156593700b5

# -*- coding: utf-8 -*-

from havenondemand.hodclient import *
import json
import pandas as pd

client = HODClient("e5504afb-4929-4b48-bf64-e156593700b5", "v1") #apikey

params = {'file': 'NAMEPLATE2.mp4', 'source_location': 'IN'} ##if using url
#params = {'file': 'E:/abcd.mp4', 'source_location': 'GB'} ## or if using a local file
response_async = client.post_request(params, 'recognizelicenseplates', async=True)
jobID = response_async['jobID']
#print jobID

## Wait some time afterwards for async call to process...
response = client.get_job_result(jobID)
print (response)

#dump data in a json file
with open('data1.json', 'w') as outfile:
    json.dump(response, outfile)