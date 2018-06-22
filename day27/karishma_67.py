# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 12:04:28 2018

@author: KARIS
"""

#importing thelibraries
import pandas as pd

#importing the dataset
dataset = pd.read_csv('movie.csv' , quoting = 3)

import re

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0,2000):
    text = re.sub('[^a-zA-Z]',' ',dataset['text'][i])
    text = text.lower()
    text = text.split()
    ps = PorterStemmer()
    text = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]
    text = ' '.join(text)
    corpus.append(text)
    
from sklearn.feature_extraction.text import CountVectorizer as CV
cv = CV(max_features= 1500)
features = cv.fit_transform(corpus).toarray()
labels = dataset.iloc[: , 0].values

from sklearn.preprocessing import LabelEncoder as LE
le = LE()
labels = le.fit_transform(labels)

from sklearn.model_selection import train_test_split as TTS
features_train, features_test , labels_train , labels_test = TTS(features , labels , test_size = 0.3 , random_state = 0)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(features_train , labels_train)

labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

