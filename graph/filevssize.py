import matplotlib.pyplot as plt
import os
from collections import defaultdict

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
    plt.pie(sizes,labels=labels)
    plt.axis('equal')
    plt.show()
pie_chart()
    