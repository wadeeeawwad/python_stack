from django.urls import path, include           
urlpatterns = [
    path('', include('first2app.urls')),
     path('blogs/', include('first2app.urls'))
    
]
