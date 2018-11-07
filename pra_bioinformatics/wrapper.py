import numpy as np
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import ExtraTreeClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def subset(data):
    m = data.shape[0]
    n = data.shape[1]
    n_b = 2**n-1
    index = np.zeros((n_b, n))
    subset_arr=np.zeros((n_b,m,n))
    temp2=str(bin(n_b-1))
    temp2=temp2[2:]
    
    for i in range(n_b):
        temp=str(bin(n_b-i))
        temp=temp[2:]
        for j in range(len(temp2)-len(temp)):
            temp='0'+temp            
        for j in range(n):
            index[i][j]=temp[j]
    
    for i in range (n_b):
        subset_arr[i]=np.where(index[i].astype(int), data, 0)
    return subset_arr


def split_features(data):
    quotient = int(data.shape[1]/15)
    reminder = int(data.shape[1]%15)
    temp_list=[]
    if quotient == 0:
        temp_list.append(data)
        
    for i in range(quotient):
        if i == quotient:
            temp_list.append(np.split(data, [15*i, 15*i+reminder], axis=1)[1])
        else:
            temp_list.append(np.split(data, [15*i, 15*(i+1)], axis=1)[1])
    return temp_list


def wrapper(tr_data, tr_ans, ts_data, ts_ans):
    
    classifiers=[SVC(), RandomForestClassifier(), LogisticRegression(), Perceptron(), ExtraTreeClassifier(), KNeighborsClassifier(), DecisionTreeClassifier()]
    split_tr_data=split_features(tr_data)
    split_ts_data=split_features(ts_data)
    result_score = 0
    result_clf = type(classifiers.__contains__)
    result_tr_data = np.zeros((tr_data.shape))
    result_ts_data = np.zeros((ts_data.shape))
    for tr, ts in zip(split_tr_data, split_ts_data):
        for  s_tr, s_ts in zip(subset(tr), subset(ts)):
            for clf in classifiers:
                clf.fit(s_tr, tr_ans)
                pred_y = clf.predict(s_ts)
                temp_score = accuracy_score(ts_ans, pred_y)
                if result_score < temp_score:
                    result_score = temp_score
                    result_clf = clf
                    result_tr_data = s_tr
                    result_ts_data = s_ts
    
    print(result_score, result_clf)            
                
    return result_tr_data, result_ts_data

