from django.shortcuts import render
from django.http import HttpResponse

def index( request ):
    return HttpResponse("hello, World. You're at the polls index.")

def contact( request ):
    return HttpResponse("You're in the Contact page of the polls.")