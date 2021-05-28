from django.db import models
class Shows(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateField()
    network = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


