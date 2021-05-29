from django.http import request
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request)
def login(request):
     return HttpResponse("login page")