from django.http  import HttpResponse
from django.shortcuts import render,redirect
from .models import Photos,Category


def home(request):
    photo = Photos.objects.all()
    return render(request,'home.html',{"photo": photo}) 

def search_category(request):
    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get('photo')
        searched_photos = Photos.search_by_photo_category(search_term)
        message = f'{search_term}'


        return render(request, 'search.html',{"message":message, "photo":searched_photos})

    else:
        message = "You haven't searched for term"
        return render(request,'search.html',{'message':message})