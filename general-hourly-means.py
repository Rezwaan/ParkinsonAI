import os 
import csv
import numpy as np
import pandas as pd
csvfiles = []
dflist=[]

status=[0,1,1,0,1,1,1,0,1,0,1,1,0,0,0]
pno=0
path1='E:\\CS\\Semester 7\\Project-1 ( Parcinson Predictor) CS 491\\Data Set\\PD'
root = os.listdir(path1) 


for patients in root:
    path2= path1+ '\\' + patients
    hourly = os.listdir(path2)
    createfile = 'E:\\CS\\Semestr 7\\Project-1 ( Parcinson Predictor) CS 491\\Data Set\\Hourly\\' + patients + '.csv'
    with open(createfile, 'wb') as PatientFile:
        fieldnames = ['mean3', 'mean6', 'mean10' , 'status']
        writer = csv.DictWriter(PatientFile, fieldnames=fieldnames)
        writer.writeheader()

    for hour in hourly:
        path3= path2 + '\\' + hour
        print path3
        files = os.listdir(path3)
        for file in files:
            if file.startswith('hdl_accel'):
                if file.endswith('.csv'):
                    n=sum(1 for line in open(os.path.join(path3, file)))
                    if(n>1000):
                        excel = pd.read_csv(os.path.join(path3, file))
                        psd3=excel[['x.PSD.3' , 'y.PSD.3' , 'z.PSD.3']].mean().mean()
                        psd6=excel[['x.PSD.6' , 'y.PSD.6' , 'z.PSD.6']].mean().mean()
                        psd10=excel[['x.PSD.10' , 'y.PSD.10' , 'z.PSD.10']].mean().mean()
                        values=[psd3, psd6, psd10, status[pno]]
                        save_mean='E:\\CS\\Semester 7\\Project-1 ( Parcinson Predictor) CS 491\\Data Set\\Hourly' + '\\' +  patients + '.csv'
                        with open(save_mean, 'ab') as save:
                            writer = csv.writer(save)
                            writer.writerow(values)
    pno+=1
                            
                    

   
    
    
    

                        
                    
                    #dflist.append(second)
                    #combined=pd.merge(apple, second , how='outer')
                    
                    
                    
                    
                    
                    
                    
#combined.to_csv('MHu.csv', index=False)
#apple = pd.read_csv("MHu.csv")
#print 'Combined : ', sum(1 for line in open("MHu.csv"))
#print 'Mean 1 : ' , apple[['x.PSD.3' , 'y.PSD.3' , 'z.PSD.3']].mean().mean()

#hsn = pd.read_csv("MHu.csv", usecols=[7,8,9,15,16,17,23,24,25])
#print 'Mean 2 : ' , hsn[['x.PSD.3' , 'y.PSD.3' , 'z.PSD.3']].mean().mean()
#directory='C:\\Users\\Hassan\\workspace\\fyp'


#concat=pd.concat(dflist, axis=0)
#concat.to_csv('apple.csv', index=None)

#data = pd.read_csv("MH.csv", usecols=[8,16,24])
#print data
#print 'Length of file : ' , sum(1 for line in open('C:\\Users\\Hassan\\workspace\\fyp\\MH.csv'))

                
                
            