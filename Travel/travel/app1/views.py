from django.shortcuts import render
from django.http import HttpResponse
from app1.models import contactP
# Create your views here.
def index(request):
    return render(request,'index.html')
def contactM(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        r=contactP(name=name,email=email,phone=phone,message=message)
        r.save()
        return render(request,'index.html',{'msg':'we will Reply as Soon as Possible'})


