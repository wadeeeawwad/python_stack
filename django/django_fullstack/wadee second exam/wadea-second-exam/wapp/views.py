from django.http import request
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
def index(request):

    context = {
        'users': User.objects.all()
    }
    return render(request, "index.html", context)

def success(request):
    context = {
        'users': User.objects.all(), 

        'allposts' : Post.objects.all()
        
    }
    return render(request,"thought.html", context)

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    if request.POST['password'] != request.POST['cpassword']:
        return redirect('/')
    request.session['username'] = request.POST['email']
    User.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
    return redirect("/thoughts")
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    user = User.objects.filter(email=request.POST['email'])
    user2 = User.objects.filter(password=request.POST['password'])
    if user:
        if user2:
            if user2[0].password == request.POST['password']:
                request.session['username'] = user[0].first_name
                request.session['id'] = user[0].id
                return redirect("/thoughts")
            else:
                return redirect('/')
        return redirect('/')
    else:
        return redirect('/')

def logout(request):
    del request.session['username']
    return redirect('/')

def addpost(request):
    theloginuser = User.objects.get(id = request.session['id'])
    Post.objects.create(post = request.POST['post'], users = theloginuser)
    return redirect("/thoughts")


def thoughts(request,id):
    this_post =  Post.objects.get(id = id)
    context={
        'this_post': Post.objects.get(id = id),
        'userid': request.session['id'],
        'test': this_post.liked_by.filter(id = request.session['id'])
    }
    return render(request,'details.html',context)

def like(request,id):
    id = id
    postliked = Post.objects.get(id = id)
    userliked = User.objects.get(id = request.session['id'])
    postliked.liked_by.add(userliked)
    return redirect('/thoughts/'+str(id))
def unlike(request,id):
    id = id
    postliked = Post.objects.get(id = id)
    userliked = User.objects.get(id = request.session['id'])
    postliked.liked_by.remove(userliked)
    return redirect('/thoughts/'+str(id))

def delete(request,id):
    d = Post.objects.get(id = id)
    d.delete()
    return redirect("/thoughts")