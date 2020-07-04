import csv
import pandas as pd
import os
import numpy as np

os.getcwd()

os.chdir('/home/devaki/Desktop/insta/NLP/how_to_preprocess/twitter')

#Load dataset of features
train_dataset = pd.read_csv('p_train.csv',header=0)

test_dataset = pd.read_csv('p_test.csv',header=0)


X_train = train_dataset.iloc[:,1:].values
y_train = train_dataset.iloc[:,0:1].values

X_test = test_dataset.iloc[:,1:].values
y_test = test_dataset.iloc[:,0:1].values


#Scaling


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#Model

from sklearn.svm import SVC

classifier = SVC(kernel = 'rbf', random_state=0)
classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)


#Confusion Matrix

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)
















