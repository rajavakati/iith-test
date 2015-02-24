# Create your views here.
#import matplotlib.pyplot as plt
import os
from collections import defaultdict

def line_chart():
    frqdic = defaultdict(int)
    typedic={}
    path= '/home/rajarrv/Desktop/test'
    for each in os.listdir(path):
        if os.path.isfile(os.path.join(path,each)):
            frqdic[os.path.splitext(each)[-1]]+=1
            print os.path.splitext(each)[-1]
    print frqdic
    y=frqdic.values()
    i=1
    for each in frqdic:
        if each=='':
            each='None'
        typedic[i]=each
        i=i+1
    print typedic  
    x=typedic.keys()
    return frqdic
    #plt.plot(x,y)
    #plt.show()

def pie_chart():
    sizdic = defaultdict(int)
    path= '/home/rajarrv/Desktop/test'
    for each in os.listdir(path):
        flpath=os.path.join(path,each)
        if os.path.isfile(flpath):
            fltyp=os.path.splitext(each)[-1]
            if fltyp=='':
                fltyp='None' 
            sizdic[fltyp]+=os.path.getsize(flpath)
            print os.path.getsize(flpath)
            print os.stat(flpath).st_size 
    labels=sizdic.keys()
    sizes=sizdic.values()
    #plt.pie(sizes,labels=labels)
    #plt.axis('equal')
    #plt.show()
    return sizdic
