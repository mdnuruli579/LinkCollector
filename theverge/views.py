from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Link
from datetime import datetime
import pandas as pd
# Create your views here.
 
def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site','')
 
        page = requests.get(site)
        soup = BeautifulSoup(page.content,'html.parser')
        # arr=soup.findAll(attrs={'class':'content'})
        # print(arr)
        filename =datetime.now().strftime("%d%m%Y") + "_verge.csv"
        for sp in soup.find_all('a'):
            address="https://www.theverge.com"+sp.get('href')
            headline=sp.string
            author=sp.get('h1')
            date=sp.get('time')
            Link.objects.create(address=address,name=headline,author=author,date=date)
            arr=[[address,headline,author,date]]
            df=pd.DataFrame(arr,columns=['url','headline','author','date'])
        df.to_csv(filename)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()
 
 
    return render(request,'theverge/index.html',{'data':data})
 
def clear(request):
    Link.objects.all().delete()
    return render(request,'theverge/index.html')