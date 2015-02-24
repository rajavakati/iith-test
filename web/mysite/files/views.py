# Create your views here.
from django.http import HttpResponse
import os
from collections import defaultdict
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index1(request):
    return "Hello, world. You're at the polls index."

@csrf_exempt
def frequency(request):
    frqdic = defaultdict(int)
    typedic={}
    path= '/home/rajarrv/Desktop/test'
    for each in os.listdir(path):
        if os.path.isfile(os.path.join(path,each)):
            frqdic[os.path.splitext(each)[-1]]+=1
            print os.path.splitext(each)[-1]
    y=frqdic.values()
    i=1
    for each in frqdic:
        if each=='':
            each='None'
        typedic[i]=each
        i=i+1
    x=typedic.keys()
    return HttpResponse(json.dumps(frqdic), content_type="application/json")

@csrf_exempt
def sizes(request):
    sizdic = defaultdict(int)
    path= '/home/rajarrv/Desktop/test'
    for each in os.listdir(path):
        flpath=os.path.join(path,each)
        if os.path.isfile(flpath):
            fltyp=os.path.splitext(each)[-1]
            if fltyp=='':
                fltyp='None' 
            sizdic[fltyp]+=os.path.getsize(flpath)
    labels=sizdic.keys()
    sizes=sizdic.values()
    #plt.pie(sizes,labels=labels)
    #plt.axis('equal')
    #plt.show()
    return HttpResponse(json.dumps(sizdic), content_type="application/json")
