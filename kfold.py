import os 
import numpy as np
import pandas as pd
import csv
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
csvfiles = []
generalpath='F:\Hourly Data\\'
#generalpath='E:\\CS\\Semester 7\\Project-1 ( Parcinson Predictor) CS 491\\Data Set\\Clustered Hourly'

list_dirs = os.listdir('F:\Hourly Data\\') 
#list_dirs = os.listdir('E:\\CS\\Semester 7\\Project-1 ( Parcinson Predictor) CS 491\\Data Set\\Clustered Hourly')

dflist=[]
array=['Apple.csv', 'Cherry.csv', 'Crocus.csv', 'Dafodil.csv' , 'Daisy.csv', 'Flox.csv' , 'Iris.csv', 'Lily.csv', 'Mapple.csv', 'Orange.csv', 'Orchid.csv', 'Peony.csv', 'Rose.csv' , 'Sunflower.csv', 'Sweatpea.csv']
checkfile=0
for i in range(0, len(list_dirs)-1):
    for file in list_dirs:
        if(file == array[checkfile]):
            print 'Leaving ' , array[checkfile] , ' for testing.'
            continue
        else:
            path= 'F:\Hourly Data\\' + file
            #path='E:\\CS\\Semester 7\\Project-1 ( Parcinson Predictor) CS 491\\Data Set\\Clustered Hourly\\' + file
            excel = pd.read_csv(path)
            dflist.append(excel)

    concat=pd.concat(dflist, axis=0)
    trainfile='F:\Hourly Data\\Without' + array[checkfile]
    #trainfile='E:\\CS\\Semester 7\\Project-1 ( Parcinson Predictor) CS 491\\Data Set\\Clustered Kfold\\Without' + array[checkfile]
    concat.to_csv(trainfile , index=None)
    
    traindata= pd.read_csv(trainfile)
    testdata = pd.read_csv(os.path.join(generalpath, array[checkfile]))
    
    features = list(testdata.columns[0:3]) 
    targets = testdata.columns[3]
    
    X_test = testdata[features]
    y_test = testdata[targets]
    
    features_train = list(traindata.columns[0:3]) ####
    targets_train = traindata.columns[3]
    
    X_intrain = traindata[features_train]
    y_intrain = traindata[targets_train]

    total_in_traindata = traindata.shape[0]
    for_train = total_in_traindata
    for_test = total_in_traindata - for_train
    
    X_train, xtest, y_train, ytest = train_test_split(X_intrain, y_intrain, test_size=for_test,random_state=2)
    
    clf = SVC()
    clf.fit(X_train, y_train) 
    SVC(gamma=10, kernel='rbf')
    
    predict = clf.predict(X_test)
    
    pdp=npd=0
    
    print 'y_test : ' , len(y_test) , ' y_predicted : ', len(predict)
    for i in range(0,len(y_test)):
        if(predict[i] == y_test[i]):
            pdp+=1
        else:
            npd+=1
    
    print 'PD (' , array[checkfile]  , '): ' , pdp
    print 'NPD (' , array[checkfile]  , '): ' , npd
    
    if(pdp > npd):
        print array[checkfile] , ' is a PD.'
    else:
        print array[checkfile] , ' is a NPD.'
    
    print '-------------------------------------------------'
    
    checkfile+=1
    pdp=npd=0
    del dflist[:]