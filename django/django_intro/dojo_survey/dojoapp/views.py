from django.shortcuts import render, HttpResponse
def index(request):
    return render(request,"index.html")
def result(request):
    name= request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']
    # print(name)
    # print(location)
    # print(language)
    # print(comment)
    context = {
    	"name" : name,
    	"language" : language,
        "location":location,
        "comment":comment
    }
    return render(request,"new.html",context)
