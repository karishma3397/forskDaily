# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:00:29 2018

@author: KARIS
"""
 
# open weather api: ff1246fde51147b9eb2b662f6e613121
import pandas as pd
df = pd.DataFrame()
#new delhi ,gurgaon,  gurugram , faridabad , noida, ghaziabad,panipat, sonipat,patparganj, burari
cities = ['VIDP','VOHS','VIDD']
import urllib.request
for city in cities:
    url = "https://www.wunderground.com/history/airport/"+city+"/2015/6/20/CustomHistory.html?dayend=20&monthend=6&yearend=2018&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo="
    page = urllib.request.urlopen(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page, "lxml")
    right_table = soup.find('table',{'id':'obsTable'})
    
    
    Temp= []
    DewPoint= []
    Humiditypercent= []
    SeaLevel= []
    Visiblity = []
    Wind = []
    rows = right_table.find_all("tr")
    for row in rows:
        
        cells = row.findAll('td')
        if len(cells)==21:
            if all(cells[i].text.strip().isdigit() for i in [2,5,8,11,14,17]):
                Temp.append(cells[2].text.strip())
                DewPoint.append(cells[5].text.strip())
                Humiditypercent.append(cells[8].text.strip())
                SeaLevel.append(cells[11].text.strip())
                Visiblity.append(cells[14].text.strip())
                Wind.append(cells[17].text.strip())
    
    df['Temp'+city]=Temp
    df['DewPoint'+city] = DewPoint
    df['Humiditypercent'+city]=Humiditypercent
    df['SeaLevel'+city] = SeaLevel
    df['Visiblity'+city]= Visiblity
    df["Wind"+city] = Wind
    
feat = df.iloc[:,6:].values
labels =df.iloc[: , :6].values
from sklearn.model_selection import train_test_split as TTS
feat_train, feat_test , labels_train , labels_test = TTS(feat , labels ,test_size = 0.2 ,random_state = 0)
'''
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
feat_train = sc.fit_transform(feat_train)
feat_test = sc.transform(feat_test)
'''
'''
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(feat_train , labels_train)
labels_pred = regressor.predict(feat_test)
'''

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
poln_object = PolynomialFeatures(degree = 2)
feat_train_poln = poln_object.fit_transform(feat_train)
feat_test_poln = poln_object.transform(feat_test)
feat_test_poln_abs = poln_object.transform(np.array([24,23,91,1007,5,19,33,25,55,999,3,6]).reshape(1,-1))
lin_reg_2 = LinearRegression()
lin_reg_2.fit(feat_train_poln,labels_train)
import numpy as np
lin_2_reg_pred = lin_reg_2.predict(feat_test_poln)
lin_2_reg_pred2 = lin_reg_2.predict(feat_test_poln_abs)
score = lin_reg_2.score(feat_test_poln , labels_test)


from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = lin_reg_2, X = feat_train_poln, y = labels_train, cv = 10)
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())