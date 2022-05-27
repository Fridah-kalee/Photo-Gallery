from django.http  import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,"home.html")

# def photos(request):
#     photo=Photos.objects.all()
#     return render(request,'photo.html',{"photo": photo}) 
