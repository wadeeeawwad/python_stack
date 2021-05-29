from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from app.models import User

def index(request):
    if 'user' in request.session:
        return redirect("/welcome")

    return render(request,'index.html')

def login(request):
    username=request.POST['username']
    passwod=request.POST['passwod']
    
def register(request):
    username=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    address=request.POST['address']
    user = User.objects.create(username=username,email=email,address=address,password=password)
    
    data={
      "username":username,
      "password":password,
      "address":address,
      "email":email,

    }
    request.session['user']= data
    return redirect("/welcome")
def welcome(request):
    if 'user' in request.session:
        username =request.session['user']['username']
        return render(request,'welcome.html')
    return redirect("/")

def logout(request):
    if 'user' in request.session:
        request.sesion.clear()
    return redirect('/')
    




