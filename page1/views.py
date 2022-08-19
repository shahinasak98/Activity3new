from django.shortcuts import render,HttpResponse
from .models import numModel
from num2words import num2words

# Create your views here.

def create(request):
    return render(request,"index.html")

def conversion(request):
    if request.method=='POST':
        numberinput=request.POST['numberinput']
        wordoutput=num2words(numberinput)
        obj=numModel.objects.create(inputnum=numberinput,outputword=wordoutput)

    return HttpResponse('The word equivalent for {} is {}'.format(numberinput,wordoutput))
