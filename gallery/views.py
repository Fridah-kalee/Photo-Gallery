from django.http  import HttpResponse
from django.shortcuts import render,redirect
from .models import Photos

# Create your views here.
# def home(request):
#     return render(request,"home.html")

def home(request):
    photo = Photos.objects.all()
    return render(request,'home.html',{"photo": photo}) 
