from django.urls import path     
from . import views

urlpatterns = [
  path('', views.index),
  path('show/new',views.add_show),
  path('shows/create',views.create),
  path('shows/<int:id>',views.display),
  path('shows/<int:id>/edit',views.edit),
  path('delete/<int:id>',views.delete),
  path('update/<int:id>',views.update)

]