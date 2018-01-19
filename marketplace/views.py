from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def list_products():
    return HttpResponse("this is market place views")
    
    
