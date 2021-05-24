from django.shortcuts import render,redirect
from .models import dojos,ninjas

def index(request):
    context = {
        'dojos' : dojos.objects.all(),
        'ninja' : ninjas.objects.all(),
    }
    return render(request,"index.html",context)

def add_dojo(request):
    name = request.POST['dojo_name']
    city = request.POST['dojo_city']
    state = request.POST['state']
    dojos.objects.create(name=name,city=city,state=state)
    return redirect('/')
def dojo_list(request):
    context = {
        'dojos' : dojos.objects.all(),
    }
    return redirect('/',context)
def add_ninja(request):
    first_from = request.POST['first_name']
    last_from = request.POST['last_name']
    # id_from =  request.POST['dojo']

    ninjas.objects.create(first_name=first_from,last_name=last_from,dojo=dojos.objects.get(id=request.POST['dojo_menu']))
    return redirect('/')