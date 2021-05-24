from django.db import models
class Books (models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Authours (models.Model):
    first_name = models.CharField(max_length=45)
    Last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Books,related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField()
