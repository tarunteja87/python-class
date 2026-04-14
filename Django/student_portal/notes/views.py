from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def greet(request):
    return HttpResponse ("Hello all something else ")

def hotels(request):
    return HttpResponse(" you are in the resturent page")