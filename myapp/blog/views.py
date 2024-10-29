from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):

    modules = [
        {'id':1,'title':'Post1','phases':'Phase-1','difficulty':'Begginer','img_url':'https://picsum.photos/200'},
        {'id':2,'title':'Post2','phases':'Phase-1','difficulty':'Begginer' ,'img_url':'https://picsum.photos/200'},
        {'id':3,'title':'Post3','phases':'Phase-1','difficulty':'Intermediate'  ,'img_url':'https://picsum.photos/200'},
    ]

    return render(request,'index.html', {'modules': modules})

def detail(request, module_id):
    return render(request,'module.html') 