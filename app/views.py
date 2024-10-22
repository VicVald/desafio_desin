from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def naves(request):
    return render(request,'naves.html')

def patos(request):
    return render(request,'patos.html')

