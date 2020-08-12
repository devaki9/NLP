import csv
import pandas as pd
import os
import numpy as np

os.chdir(os.getcwd())

#Load dataset of features
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('cleaned_ds.csv',header=0)

#split into test train

X = dataset.iloc[:,1:].values
y = dataset.iloc[:,0:1].values

X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.5,random_state=0)

#Scaling


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""
================================================================================
                        APPLYING VARIOUS MODELS
==============================================================================
1.)SUPPORT VECTOR CLASSIFIER
"""

from sklearn.svm import SVC

classifier = SVC(kernel = 'linear', random_state=0)
classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)


#Confusion Matrix

from sklearn.metrics import confusion_matrix, classification_report

cm = confusion_matrix(y_test, y_pred)

print(np.isnan(cm.data).any())

print("------------------------------------------------------------")
print('\tSupport Vector Classifier')
print(cm)

accuracy = (cm[0][0]+cm[1][1])/(cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1])
print('Accuracy for SVC=',accuracy*100,'%') #59.4%

print('For SVM:',classification_report(y_test, y_pred))
print("------------------------------------------------------------")

#2.)NAIVE BAYES 

from sklearn.naive_bayes import GaussianNB

classifier_nb = GaussianNB()

classifier_nb.fit(X_train,y_train)

y_pred_nb = classifier_nb.predict(X_test)

from sklearn.metrics import confusion_matrix

cm_nb = confusion_matrix(y_test, y_pred_nb)
print("\n------------------------------------------------------------")
print('\tNaive Bayes')
print(cm_nb)

accuracy_nb = (cm_nb[0][0]+cm_nb[1][1]) / (cm_nb[0][0]+cm_nb[0][1]+cm_nb[1][0]+cm_nb[1][1])
print('Accuracy for Naive Bayes = ',accuracy_nb*100,'%') #55.6%

print('For Naive Bayes:',classification_report(y_test, y_pred_nb))
print("------------------------------------------------------------")

#3.)DECISION TREE CLASSIFIER

from sklearn.tree import DecisionTreeClassifier

#same results for:
#gini,max_depth=100,random_state=1

classifier_dt = DecisionTreeClassifier(criterion = 'entropy',max_depth=100, random_state = 0)
classifier_dt.fit(X_train, y_train)

y_pred_dt = classifier.predict(X_test)

cm_dt = confusion_matrix(y_test, y_pred_dt)
print("\n------------------------------------------------------------")
print('\tDecisionTreeClassifier')
print(cm_dt)

accuracy_dt = (cm_dt[0][0]+cm_dt[1][1]) / (cm_dt[0][0]+cm_dt[0][1]+cm_dt[1][0]+cm_dt[1][1])
print('Accuracy for Decision Tree = ',accuracy_dt*100,'%') #

print('For Decision Tree:',classification_report(y_test, y_pred_dt))
print("------------------------------------------------------------")


#4.)KNN
from sklearn.neighbors import KNeighborsClassifier

mod = KNeighborsClassifier(n_neighbors=10)

mod.fit(X_train,y_train)
y_pred_knn = mod.predict(X_test)

print("\n------------------------------------------------------------")
print('\tKNN')
cm_knn=confusion_matrix(y_test, y_pred_knn)
print(cm_knn)

accuracy_knn = (cm_knn[0][0]+cm_knn[1][1]) / (cm_knn[0][0]+cm_knn[0][1]+cm_knn[1][0]+cm_knn[1][1])
print('Accuracy for KNN = ',accuracy_knn*100,'%') 

c_report=classification_report(y_test, y_pred_knn)

print(c_report)
print("------------------------------------------------------------")


#5.)Random Forest Classifier

from sklearn.ensemble import RandomForestClassifier

classifier_rf = RandomForestClassifier(n_estimators=10,criterion='gini',random_state=0)
classifier_rf.fit(X_train,y_train)

y_pred_rf = classifier_rf.predict(X_test)
print("\n------------------------------------------------------------")
print('\tRandom Forest Classifier')
cm_rf =confusion_matrix(y_test, y_pred_rf)
print(cm_rf)

accuracy_rf =  (cm_rf[0][0]+cm_rf[1][1]) / (cm_rf[0][0]+cm_rf[0][1]+cm_rf[1][0]+cm_rf[1][1])
print('Accuracy for Random Forest Classifer = ',accuracy_rf*100)
print('For Random Forest Classifer:',classification_report(y_test, y_pred_rf))
print("------------------------------------------------------------")



from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

classifier=LogisticRegression(random_state=0)
classifier.fit(X_train,y_train)

y_pred_lr=classifier.predict(X_test)


cm_lr =confusion_matrix(y_test, y_pred_lr)
print(cm_lr)

accuracy_lr =  (cm_lr[0][0]+cm_lr[1][1]) / (cm_lr[0][0]+cm_lr[0][1]+cm_lr[1][0]+cm_lr[1][1])
print('Accuracy for Logistic Regression = ',accuracy_lr*100)
print('For Logistic Regression:',classification_report(y_test, y_pred_lr))
print("------------------------------------------------------------")



#count number of 0's in y_test
count_ones=0
for x in y_test:
    if x==1:
        count_ones+=1

print('count_ones=',count_ones)
print('count_zeroes=',(800-count_ones))