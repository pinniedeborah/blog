from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import request
from .models import Post,Comment

def home(request):
    pv=Post.objects.all()
    context={
        "pv":pv
    }
    return render(request,"index.html", context)

def about(request):
    return render(request,"about.html")
# Create your views here.
