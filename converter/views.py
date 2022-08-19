from django.shortcuts import render,HttpResponse

# Create your views here.

def create(request):
    return render(request,"index.html")

def conversion(request):
    return HttpResponse('request recieved')