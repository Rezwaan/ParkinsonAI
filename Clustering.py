import numpy as np
import csv as csv
import pandas as pd
from pandas.core.frame import  DataFrame
import sklearn
import matplotlib.pyplot as plt
from matplotlib import style
from scipy.cluster.hierarchy import centroid
from matplotlib.pyplot import colors
from numpy.distutils.conv_template import header
from numpy import dtype
from array import array
from mhlib import FOLDER_PROTECT
import Noisy_Removal
style.use("ggplot")
import os
import glob
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from Noisy_Removal import Noisy
from scipy.spatial.distance import euclidean

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def non_numeric(self,df):
        columns=df.columns
        for column in columns:
            text_dig={}
            def convert_to_int(val):
                return text_dig[val]
            if df[column].dtype != np.int64 and df[column].dtype != np.float64:
                col_contents=df[column].values.tolist()
                unique_ele=set(col_contents)
                x=0
                for unique in unique_ele:
                    if unique not in text_dig:
                        text_dig[unique]=x
                        x+=1
                df[column]=list(map(convert_to_int, df[column]))
        return df
    
    def graphss(self):
        noisy=Noisy()
        
        
        my_dir = "G:\\Mjff DataSet\\MJFF DATASET\\MJFF-Data\\tar\\"
        filelist = []
        os.chdir( my_dir )
        folder_name=[]
        csv_name=''
        i=0
        
        for names in glob.glob( "HumDynLog*" ) :
            folder_name.append(names)
            i=+1
        '''
        for f in range(0,len(folder_name)):
            if (folder_name[f]=="HumDynLog_SUNFLOWER_LGE_LGE_a000002887faa3_20120129_065146_20120129_070000"):
                print f
        '''    
            
        
        retval = os.getcwd()
        print retval
        print len(folder_name)
        
        for i in range(0,len(folder_name)):
            my_dir = "G:\\Mjff DataSet\\MJFF DATASET\\MJFF-Data\\tar\\"+folder_name[i]+"\\"
            #print folder_name[i]
            os.chdir( my_dir )
            print my_dir
            switch=True
            if (glob.glob("*hdl_accel_*.csv") and glob.glob("*hdl_cmpss_*.csv") and switch==True):
                switch=False
                if (glob.glob("*hdl_cmpss_*.csv")):
                    for name in glob.glob("*hdl_cmpss_*.csv"):
                        a=pd.read_csv(name)
                else:
                    print "No hdl_cmpss"
                if (glob.glob("*hdl_gps_*.csv")):
                    for name in glob.glob("*hdl_gps_*.csv"):
                        b=pd.read_csv(name)
                else:
                    for name in glob.glob("*hdl_cmpss_*.csv"):
                        b=pd.read_csv(name)
                
                merged=a.merge(b,on='time')
                merged.to_csv("clustering.csv",index=False)
                csv_name=glob.glob("*hdl_accel_*.csv")
                #print "csvName"
                #print csv_name[0]
                data = pd.read_csv('clustering.csv', delimiter=',')
                data1=pd.read_csv(csv_name[0],delimiter=',')
                #data1=self.non_numeric(data1)
                data=self.non_numeric(data)
                
                #print (data1)
                
                #print "CLustering Data/////"
                #combined_data = data
                
                #print data
                
                if (len(data.index)<=9):
                    print "Too Low"
                else:
                    array_convt = data.values
                    #print array_convt
                    data.head()
                    t_data=PCA(n_components=2).fit_transform(array_convt)
                    #print t_data
                    k_means=KMeans(n_clusters=10)
                    k_means.fit_predict(t_data)
                        #------------k means fit predict method for testing purpose-----------------
                    clusters=k_means.fit_predict(t_data)
                    #print clusters.shape
                        
                    cluster_0=np.where(clusters==0)
                    cluster_1=np.where(clusters==1)
                    cluster_2=np.where(clusters==2)
                    cluster_3=np.where(clusters==3)
                    cluster_4=np.where(clusters==4)
                    cluster_5=np.where(clusters==5)
                    cluster_6=np.where(clusters==6)
                    cluster_7=np.where(clusters==7)
                    cluster_8=np.where(clusters==8)
                    cluster_9=np.where(clusters==9)
                    X_cluster_0 = t_data[cluster_0]
                    X_cluster_1 = t_data[cluster_1]
                    X_cluster_2 = t_data[cluster_2]
                    X_cluster_3 = t_data[cluster_3]
                    X_cluster_4 = t_data[cluster_4]
                    X_cluster_5 = t_data[cluster_5]
                    X_cluster_6 = t_data[cluster_6]
                    X_cluster_7 = t_data[cluster_7]
                    X_cluster_8 = t_data[cluster_8]
                    X_cluster_9 = t_data[cluster_9]
                            
                    add=len(X_cluster_0)+len(X_cluster_1)+len(X_cluster_2)+len(X_cluster_3)+len(X_cluster_4)+len(X_cluster_5)+len(X_cluster_6)+len(X_cluster_7)+len(X_cluster_8)+len(X_cluster_9)
                        #for i in range(0,10):
                                #add=+len(X_cluster[i])
                    #print ('totals are: ',add)
                        
                        
                            
                    distance1=0.0
                    invalid=[]
                        
                    for i in range(0,len(X_cluster_0)):
                        distance1 += euclidean(X_cluster_0[i], k_means.cluster_centers_[0])
                            #print ('distance of first cluster :',distance1)
                    mean_dist1=distance1/len(X_cluster_0)
                            #print ('Mean distance is : ',mean_dist1)
                    if len(X_cluster_0)<10 or mean_dist1>=1.5:
                        for i in range(0,add):
                            if(k_means.labels_[i]==0):
                                invalid.append(i)
                        #print invalid
                        
                        
                            #Noisy Data Removal...///
                    distance1=0.0
                            
                    for i in range(0,len(X_cluster_1)):
                        distance1 += euclidean(X_cluster_1[i], k_means.cluster_centers_[1])
                            #print ('distance of first cluster :',distance1)
                    mean_dist1=distance1/len(X_cluster_1)
                            #print ('Mean distance is : ',mean_dist1)
                    if len(X_cluster_1)<10 or mean_dist1>=1.5:
                        for i in range(0,add):
                            if(k_means.labels_[i]==1):
                                invalid.append(i)
                        #print invalid
                            
                            
                            
                    distance1=0.0
                    for i in range(0,len(X_cluster_2)):
                        distance1 += euclidean(X_cluster_2[i], k_means.cluster_centers_[2])
                            #print ('distance of first cluster :',distance1)
                    mean_dist1=distance1/len(X_cluster_2)
                            #print ('Mean distance is : ',mean_dist1)
                    if len(X_cluster_2)<10 or mean_dist1>=1.5:
                        for i in range(0,add):
                            if(k_means.labels_[i]==2):
                                invalid.append(i)
                        #print invalid
                            
                            
                    distance1=0.0
                    for i in range(0,len(X_cluster_3)):
                        distance1 += euclidean(X_cluster_3[i], k_means.cluster_centers_[3])
                            #print ('distance of first cluster :',distance1)
                    mean_dist1=distance1/len(X_cluster_3)
                            #print ('Mean distance is : ',mean_dist1)
                    if len(X_cluster_3)<10 or mean_dist1>=1.5:
                        for i in range(0,add):
                            if(k_means.labels_[i]==3):
                                invalid.append(i)
                        #print invalid
                            
                            
                    distance1=0.0
                    for i in range(0,len(X_cluster_4)):
                        distance1 += euclidean(X_cluster_4[i], k_means.cluster_centers_[4])
                            #print ('distance of first cluster :',distance1)
                    mean_dist1=distance1/len(X_cluster_4)
                            #print ('Mean distance is : ',mean_dist1)
                    if len(X_cluster_4)<10 or mean_dist1>=1.5:
                        for i in range(0,add):
                            if(k_means.labels_[i]==4):
                                invalid.append(i)
                        #print invalid
                        
                            
                            
                    distance1=0.0
                    for i in range(0,len(X_cluster_5)):
                        distance1 += euclidean(X_cluster_5[i], k_means.cluster_centers_[5])
                            #print ('distance of first cluster :',distance1)
                    mean_dist1=distance1/len(X_cluster_5)
                            #print ('Mean distance is : ',mean_dist1)
                    if len(X_cluster_5)<10 or mean_dist1>=1.5:
                        for i in range(0,add):
                            if(k_means.labels_[i]==5):
                                invalid.append(i)
                        #print invalid
                            
                            
                    distance1=0.0
                    for i in range(0,len(X_cluster_6)):
                        distance1 += euclidean(X_cluster_6[i], k_means.cluster_centers_[6])
                            #print ('distance of first cluster :',distance1)
                    mean_dist1=distance1/len(X_cluster_6)
                            #print ('Mean distance is : ',mean_dist1)
                    if len(X_cluster_6)<10 or mean_dist1>=1.5:
                        for i in range(0,add):
                            if(k_means.labels_[i]==6):
                                invalid.append(i)
                        #print invalid
                            
                    distance1=0.0
                    for i in range(0,len(X_cluster_7)):
                        distance1 += euclidean(X_cluster_7[i], k_means.cluster_centers_[7])
                            #print ('distance of first cluster :',distance1)
                    mean_dist1=distance1/len(X_cluster_7)
                            #print ('Mean distance is : ',mean_dist1)
                    if len(X_cluster_7)<10 or mean_dist1>=1.5:
                        for i in range(0,add):
                            if(k_means.labels_[i]==7):
                                invalid.append(i)
                        #print invalid
                                
                                
                            
                    distance1=0.0
                    for i in range(0,len(X_cluster_8)):
                        distance1 += euclidean(X_cluster_8[i], k_means.cluster_centers_[8])
                            #print ('distance of first cluster :',distance1)
                    mean_dist1=distance1/len(X_cluster_8)
                            #print ('Mean distance is : ',mean_dist1)
                    if len(X_cluster_8)<10 or mean_dist1>=1.5:
                        for i in range(0,add):
                            if(k_means.labels_[i]==8):
                                invalid.append(i)
                        #print invalid
                            
                            
                            
                    distance1=0.0
                    for i in range(0,len(X_cluster_9)):
                        distance1 += euclidean(X_cluster_9[i], k_means.cluster_centers_[9])
                            #print ('distance of first cluster :',distance1)
                    mean_dist1=distance1/len(X_cluster_9)
                            #print ('Mean distance is : ',mean_dist1)
                    if len(X_cluster_9)<10 or mean_dist1>=1.5:
                        for i in range(0,add):
                            if(k_means.labels_[i]==9):
                                invalid.append(i)
                        #print invalid
                    print csv_name[0]
                    #noisy.noisy_removal(invalid,"clustering.csv",csv_name[0])
                    
                    
                    data1=pd.read_csv(csv_name[0],delimiter=',')
                    data1=self.non_numeric(data1)
                    
                    data1.to_csv("accel_new.csv")    
                    #3with open('accel_new.csv','w') as fp:
                        #a=csv.writer(fp,delimiter=',')
                        #print data1
                        #a.writerow(data1) 
                    
                        
                    df=DataFrame()
                    df_write = pd.DataFrame()
                    df_write=pd.read_csv("clustering.csv",delimiter=',')
                    #print "before removing invlidsss/////////////////"
                    #print df_write
                    df_write.drop(invalid)
                    
                    #print "AFTER removing invlidsss/////////////////"
                    #print df_write
                    df_write.to_csv("clustering_new.csv")
                    #data = pd.read_csv("clustering_new.csv", delimiter=',')
                    #data=self.non_numeric(data)
                    #data.to_csv("clustering_new.csv", sep='\t')
                    #with open('clustering_new.csv','w') as fp:
                        #a=csv.writer(fp,delimiter=',')
                        #a.writerow(data)
                    data=pd.read_csv("clustering_new.csv",delimiter=',')
                    data=self.non_numeric(data)
                    
                    data.to_csv("clustering_new.csv")
                    for name in glob.glob("clustering_new.csv"):
                        a=pd.read_csv(name)
                    for name in glob.glob("accel_new.csv"):
                        b=pd.read_csv(name)
                    merged=a.merge(b,on='time')
                    merged.to_csv("New_Accel_Data.csv",index=False)
                    print ('++++++++++++')   
            else:
                print "NOT FOUND"  
                     
        