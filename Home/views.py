from django.shortcuts import render

def home(request):
    return render(request,'Home/home.html')

# Create your views here.
