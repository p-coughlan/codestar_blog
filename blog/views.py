from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function to return text string to the browser
def my_blog(request):
    return HttpResponse('Hello Blog!')
