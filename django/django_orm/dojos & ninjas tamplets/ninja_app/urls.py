from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
 
  
    path('dojos',views.add_dojo),
    path('dojolist',views.dojo_list),
    path('ninja',views.add_ninja),
    

    ]
