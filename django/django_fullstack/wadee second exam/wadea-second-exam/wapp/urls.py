from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('thoughts', views.success),
    path('logout',views.logout),
    path('addpost', views.addpost),
    path('delete/<int:id>', views.delete),
    path('thoughts/<int:id>', views.thoughts),
    path('like/<int:id>', views.like),
    path('unlike/<int:id>', views.unlike),
]
