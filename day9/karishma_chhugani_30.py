# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:33:46 2018

@author: KC
"""

import urllib.request
url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
page = urllib.request.urlopen(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page, "lxml")
right_table = soup.find_all('table')
A = []
B = []
C = []
D = []
E = []
for row in right_table[0].find_all("tr"):
    cells = row.findAll('td')
    if len(cells)==5:
        A.append(cells[0].find(text=True))
        B.append(cells[1].text.strip())
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))

import pandas as pd
df = pd.DataFrame(A,columns=['pos'])
df['Team']=B
df['Matches']=C
df['Points'] = D
df['Rating']= E