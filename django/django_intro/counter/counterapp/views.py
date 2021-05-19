from django.shortcuts import redirect, render, HttpResponse
def index(request):
    if "counter" not in request.session:
        request.session["counter"]=0
    request.session["counter"]+=1
    
    return render(request,"index.html")
def destroy(request):
    request.session["counter"]=0
    return redirect("/")
def add2(request):
    request.session["counter"]+=1
    context={
        "numx":2
    }
    return render(request,"index.html",context)
def addx(request):
    num=int(request.POST["x"])

    request.session["counter"]+=num-1
    context={
        "numx":num
    }
    return render(request,"index.html",context)
    
    