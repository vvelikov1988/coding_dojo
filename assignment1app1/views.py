from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    response = redirect('/')
    return(response)

def show(request, number):
    return HttpResponse (f"placeholder to display blog number {number}.")

def edit(request, number):
    return HttpResponse (f"placeholder to edit blog {number}.")

def destroy(request, number):
    response = redirect('/')
    return(response)
