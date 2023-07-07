from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def TAB(request):
    return render(request,'Artist1.html')

def LK(request):
    return render(request,'Artist2.html')

def LP(request):
    return render(request,'Artist3.html')

def SGS(request):
    return render(request,'Artist4.html')

def TC(request):
    return render(request,'Artist5.html')


def TL(request):
    return render(request,'Artist6.html')

def JM(request):
    return render(request,'Artist7.html')

def JT(request):
    return render(request,'Artist8.html')

def MS(request):
    return render(request,'Artist9.html')








