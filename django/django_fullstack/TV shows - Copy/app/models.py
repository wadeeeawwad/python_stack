from django.db import models

class ShowsManager(models.Manager):
    def add_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 Characters long"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 Characters long"
        if len(postData['description']) < 10 :
            errors["desc"] = "Description should be at least 10 Characters long"
        return errors



        
    def edit_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 Characters long"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 Characters long"
        if len(postData['desc']) < 10 :
            errors["desc"] = "Description should be at least 10 Characters long"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateField()
    network = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()  


