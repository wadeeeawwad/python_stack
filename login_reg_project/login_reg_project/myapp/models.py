from django.db import models
class User(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)