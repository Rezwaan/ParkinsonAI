import pandas as pd
from pandas.core.frame import  DataFrame
import os
import glob

'''
Created on Nov 29, 2016

@author: Rizwan Javed
'''

class Noisy(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def noisy_removal(self,invalid,clusetering_name,accel_name):
        #obj=MyClass()
        #data = pd.read_csv(clusetering_name, delimiter=',')
        #data1=pd.read_csv(accel_name,delimiter=',')
        #data1=obj.non_numeric(data1)
        #data=obj.non_numeric(data)
            
        df=DataFrame()
        df_write = pd.DataFrame()
        df_write=pd.read_csv(clusetering_name)
        df_write.drop(invalid, inplace=True)
        df_write.to_csv(clusetering_name,index=False)
        for name in glob.glob(clusetering_name):
            a=pd.read_csv(name)
        for name in glob.glob(accel_name):
            b=pd.read_csv(name)
        merged=a.merge(b,on='time')
        merged.to_csv("New_Accel_Data.csv",index=False)
        print ('++++++++++++')