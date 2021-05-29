from django.http.response import HttpResponse
from django.shortcuts import render,redirect,HttpResponse
from myapp.models import User
def index(request):
    if "user" in request.session:
        return redirect("/welcome")
    else:
        return render(request,"index.html")
def login(request):
        username=request.POST["username"]
        passwd=request.POST["passwd"]
        if request.POST["username"] != "" and request.POST["passwd"] !="":
            users=User.objects.filter(username=username)
            user=users.first()             
            if user.username == username and user.password == passwd :
                if user.password==user.password: 
                    data={
                            "username":user.username,
                            "password":user.password,
                            "email":user.email,
                            "address":user.address
                        }
                    request.session["user"]=data
                    return redirect("/welcome")
                return redirect("/")
            return redirect("/")
                # for i in User.objects.all():
                #     if username==i.username and passwd==i.password:
                #         data={
                #             "username":i.username,
                #             "password":i.password,
                #             "email":i.email,
                #             "address":i.address
                #         }
                #         request.session["user"]=data
                #         return redirect("/welcome")
        return redirect("/")
    # username =request.POST['username']
    # passwd =request.POST['passwd']
    # users =User.objects.filter(username = username)
    # if len(users) ==0:
    #     return redirect('/')
    # user =users.first()
    # if  user.password != passwd:
    #     return redirect('/')
    # data={
    #     "username":user.username,
    #     "password":user.password,
    #     "address":user.address,
    #     "email":user.email
    # }
    # request.session['user'] = data
    # return redirect("/welcome")
def reg(request):
    username=request.POST["username"]
    email=request.POST["email"]
    address=request.POST["address"]
    passwd=request.POST["passwd"]
    data={
        "username":username,
        "password":passwd,
        "email":email,
        "address":address
    }
    user=User.objects.create(username=username,email=email,address=address,password=passwd)
    request.session["user"]=data
    return redirect("/welcome")
def welcome(request):
    if "user" in request.session:
        user=request.session["user"]
        return render(request,"welcome.html",user)
    return redirect("/")
def logout(request):
    if "user" in request.session:
        request.session.clear()
        return redirect("/")
    return redirect("/")