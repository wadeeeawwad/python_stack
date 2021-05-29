from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    # path('registration', views.add),	
    path('registration', views.add),
    path('sucsess', views.sucsess),	
    path('logout', views.logout),	
    path('login', views.login)	
    
]