from django.shortcuts import render
from time import gmtime, localtime, strftime
    
def index(request):
    context = {
        "time": strftime("%b %d, %Y %H:%M %p", localtime())

    }
    return render(request, 'index.html', context)
