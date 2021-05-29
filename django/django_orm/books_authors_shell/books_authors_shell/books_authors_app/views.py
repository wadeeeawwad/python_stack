from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def index(req):
    context = {
        "books" : Books.objects.all(),
        "authors" : Authours.objects.all()
    }
    return render(req,"index.html",context)
def addbook(req):
    title = req.POST['title']
    desc = req.POST['desc']
    Books.objects.create(title = title , desc = desc)
    return redirect("/")
def view(req,id):
    book_to_show = Books.objects.get(id=id)
    book_authours = book_to_show.authors.all()
    authours_show = Authours.objects.all()
    data = {
        'booktitle':book_to_show.title,
        'bookid' : book_to_show.id,
        'bookdesc':book_to_show.desc,
        'bookauthors':book_authours,
        'dropdwnauthors':authours_show
    }
    return render(req,"BooksView.html",data)
def addauthor(req,id):
    book= Books.objects.get(id=id)
    author = Authours.objects.get(id=req.POST['showauthor'])
    author.books.add(book)
    return  redirect("/")
    
def indexx(req):
   
    return render(req,"show.html")

def addshow(reques):
    title = req.POST['title']

    desc = req.POST['desc']
    releasedate = req.POST['releasedate']
    network = req.POST['network']

    Books.objects.create(title = title , desc = desc)
    return redirect("/")




    return redirect('/')
