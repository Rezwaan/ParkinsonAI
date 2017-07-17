import matplotlib.pyplot as plt
from matplotlib import style
from pip._vendor.html5lib.treebuilders._base import Marker
from numpy import append
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans
#from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import os
import glob
import csv as csv
import pandas as pd
'''
Created on Nov 11, 2016

@author: Rizwan Javed
'''

class MyClass1(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def training(self):
        
        my_dir = "G:\\Mjff DataSet\\MJFF DATASET\\MJFF-Data\\tar\\HumDynLog_APPLE_LGE_LGE_A0000028AF9C96_20111220_150608_20111220_160000\\"
        filelist = []
        os.chdir( my_dir )
        
        for files in glob.glob("*.csv"):
            if (glob.glob("*hdl_cmpss_*.csv")):
                        print ('chal rha hae')
                        for name in glob.glob("*hdl_cmpss_*.csv"):
                            a=pd.read_csv(name)
                        for name in glob.glob("*hdl_gps_*.csv"):
                            b=pd.read_csv(name)
                        merged=a.merge(b,on='time')
                        merged.to_csv("clustering.csv",index=False)
            else:
                print ('chal rha hae else')
                for name in glob.glob("*hdl_gps_*.csv"):
                    os.rename(name, 'clustering_gps_only.csv')
        x=[1,2,3,4,5,6,7,8,9]
        y=[9,8,7,6,5,4,32,2,1]
        z=[12,3,54,32,65,67,87,89,6]
        #X=np.array([x,y,z])
        
        X=[0,0,0]
        for i in range(len(x)):
            X=append(X,np.array([x[i],y[i],z[i]]))
        
        X=np.array([x])
        Y=np.array([y])
        Z=np.array([z])
        
        #pca=PCA(copy=True,n_components=1,whiten=False)
        #pca.fit(X)
        #X1=pca.transform(X)
        print X
        print ('printing reduce dimensions:')
        #print X1
        
        
        #ax = Axes3D(plt.gcf())
        #ax.scatter(X[:,0],X[:,1],X[:,2],s=150)
        #plt.scatter(X[:0],X[:1],X[:2],s=150)
        #plt.show()
        
        
        clf=KMeans(n_clusters=2)
        clf.fit(X,Y)
        centroids=clf.cluster_centers_
        labels=clf.labels_
        colors=["g.","r.","c.","b.","k.","o."]
        
        ax = Axes3D(plt.gcf())
        print len(X)
        ax.scatter(X[:,0],X[:,1],X[:,2],s=150)
        print X[1:,0]
        ax.scatter(centroids[:,0],centroids[:,1],centroids[:,2],marker='x',s=150)
        plt.show()
        
        