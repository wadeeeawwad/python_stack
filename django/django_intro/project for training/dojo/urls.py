from django.urls import path, include           # import include
# from django.contrib import admin              # comment out, or just delete
urlpatterns = [
    path('', include('dojoapp.urls')),
# path('admin/', admin.sites.urls)         # comment out, or just delete
]