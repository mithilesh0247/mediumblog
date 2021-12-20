from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

# Create your views here.
def blogdata(request):
    #res=requests.get('https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@mithileshpandey_48083')
    res=requests.get('https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@mithileshpandey_48083')
    data=res.json()
    data={'data':json.loads(res.content)}   
    print(data)
    return render(request,'data.html',context=data)

