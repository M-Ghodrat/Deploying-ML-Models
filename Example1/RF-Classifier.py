import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model

df = pd.read_csv('prices.csv')

x = df[df.columns.difference(['Value'])]
y = df['Value']
       
# classifier = RandomForestClassifier()
classifier = linear_model.LinearRegression()
classifier.fit(x, y)

import pickle
pickle.dump(classifier, open('classifier.pkl','wb'))
