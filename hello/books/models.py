from django.db import models

# Create your models here.
class Publisher(models.Model):
     name=models.CharField(max_length=30)
     city=models.CharField(max_length=60)
     website=models.URLField()



class Author(models.Model):
     first_name=models.CharField(max_length=30)
     last_name=models.CharField(max_length=30)
     email=models.EmailField()
