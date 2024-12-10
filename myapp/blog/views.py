from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Module
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ModuleSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import JsonResponse

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

class AddModule(APIView):
    def post(self, request):
        #Deserialize incoming JSON data
        serializer = ModuleSerializer(data=request.data)

        #Check if data is valid
        if serializer.is_valid():
            #save the new data to the db
            serializer.save()
            return Response(
                {
                    "message":"Module Created successfully!"
            
                },
                status=status.HTTP_201_CREATED
            )
        else:
            #return validation errors if data is invalid
            return Response(
                {
                    "message":"Failed to create module.",
                    "errors":serializer.errors
                },
                status=status.HTTP_404_BAD_REQUEST
            )











       