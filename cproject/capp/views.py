from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def cs(request):
    return render(request,'cs.html')

def bio(request):
    return render(request,'biology.html')

def com(request):
    return render(request,'commerce.html')

def hum(request):
    return render(request,'humanities.html')

def pe(request):
    return render(request,'pe.html')


