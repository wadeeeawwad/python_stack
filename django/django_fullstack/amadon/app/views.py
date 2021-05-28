from django.shortcuts import redirect, render, HttpResponse
from .models import *
def index(request):
    context={
     "products":product.objects.all()
     }
    
    return render(request,"index.html",context)


def checkout(request):
    quantity_from_post=int(request.post["quantity"])
    price_from_post=float(request.post["price"])
    total_charge = quantity_from_post * price_from_post
    print("Charging credit card...")
    Orderd=Order.objects.create(quantity_ordered=quantity_from_post,total_price=total_charge)
    return render(request,"checkout.html")










