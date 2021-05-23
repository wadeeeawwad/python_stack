# other imports
from django.shortcuts import redirect, render
from .models import users

# show all of the data from a table
def index(request):
    context = {
    	"users": users.objects.all()
    }
    return render(request, "index.html", context)


    
def add(request):
    users.objects.create(first_name=request.POST["first_name"],email=request.POST["email"],age=request.POST['age'])
    return redirect("/")
# def add(request):
#     users.objects.create(last_name=request.POST["last_name"])
#     return redirect("/")