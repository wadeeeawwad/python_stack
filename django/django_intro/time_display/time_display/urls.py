from django.urls import path, include         

urlpatterns = [
    path('', include('time_displayapp.urls')),
    ]
