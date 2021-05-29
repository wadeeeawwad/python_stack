from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages
from .models import *







def index(request):

    show = Shows.objects.all()
    context={
        "all_shows":show
    }

    print(context)
    return render (request,"index.html",context)

def add_show(request):
    return render(request,"new.html")

def create(request):
    if request.method =="POST":

        errors = Shows.objects.add_validator(request.POST)
        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/show/new')
        else:
            Shows.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'], 
            description=request.POST['description'])
            lastshow=Shows.objects.last()
            id=lastshow.id
            return redirect(f'/shows/{id}')


def display(request,id):
    context={
        'show':Shows.objects.get(id=id)


        


    }


    return render(request,"shows2.html",context)


def edit(request,id):

    context={
        "show":Shows.objects.get(id=id)

    }
    
    return render(request,"edit.html",context)

def update(request,id):

    errors = Shows.objects.add_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('show/new')
    else:
        if  request.method =="POST":
            update_this_show=Shows.objects.get(id=id)
            update_this_show.title=request.POST["title"]
            update_this_show.network=request.POST["network"]
            update_this_show.description=request.POST["description"]
            update_this_show.release_date=request.POST["release_date"]
            update_this_show.save()
        return redirect("/")
        

def delete(request,id):
   this_show= Shows.objects.get(id=id)
   this_show.delete()

   print("llllllllllllllll")


   return redirect('/')

                   
def update_add(request):
    errors = Shows.objects.add_validator(request.POST)
    if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('show/new')
   
       












   

 


    
    