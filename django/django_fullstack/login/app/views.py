from django.shortcuts import render,redirect
from django.contrib import messages
import re
from .models import *
import bcrypt
import datetime
def index(request):
    return render(request,'index.html')
def add(request):
    EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')
    errors={}
    if len(request.POST['fname']) < 2:
        errors['fname']="the first name should be more 2 charachter"
        

    if len(request.POST['lname'])<2:
        errors['lname']="the last name should be more 2 charachter"
        

    if not EMAIL_REGEX.match(request.POST['email']):
        errors['email']="Please enter a valid Email"
        
    
    email_user = request.POST['email']
    email_db = User.objects.filter(email = email_user)
    if len(email_db) > 0:
        errors['check_email']="email is exist"
        

    if len(request.POST['password'])<8:
        errors['password']="short password"
        

    if request.POST["password"]!=request.POST['confirm_pw']:
        errors['confirm_pw']="not maching" 
        
    for key,value in errors.items():
        if len(errors) > 0 :
            messages.error(request,value)
            return redirect('/')
            

    else:
        
        first=request.POST["fname"]
        last=request.POST["lname"]
        em=request.POST["email"]
        pas=request.POST["password"]
        conf=request.POST["confirm_pw"]
        print('111111111111111111111111111111111')
        if pas==conf:
            print('22222222222222222222222222222222')
            hash1 = bcrypt.hashpw(pas.encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name=first,last_name=last,email=em,password=hash1)
            if 'fullname' not in request.session:
                request.session['fullname']=first
                print('333333333333333333333333333333333')
                # request.session['key']=value
            return redirect("/sucsess")
    return redirect('/')

def sucsess(request):
    return render(request,"sucsess.html")

def logout(request):
    del request.session['fullname']
    return redirect("/")

def login(request):
    user=User.objects.filter(email=request.POST['lemail'])
    if user: #if len(user) 
        if bcrypt.checkpw(request.POST['lpassword'].encode(),user[0].password.encode()):
            if 'fullname' not in request.session: #to save the session in the prowser
                request.session['fullname']=user[0].first_name
            return redirect("/sucsess")
    return redirect('/')
    
        



        
