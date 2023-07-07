from django.shortcuts import render
from .models import Song

# Create your views here.
def SWA(request):
    AllSongs = Song.objects.all()
    return render(request,'Cat/SWA1.html',context={"AllSongs": AllSongs})