from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gallery(request):
    return HttpResponse('hello')
