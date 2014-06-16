from django.db import models

# Create your models here.

# Create your models here.
class Artist(models.Model):
     name=models.CharField(max_length=30)
     age=models.IntegerField(max_length=60)

     def __unicode__(self):
	return self.name
     

class Album(models.Model):
     performer=models.CharField(max_length=30)
     name=models.CharField(max_length=30)
     desc=models.CharField(max_length=30)
     year=models.IntegerField(max_length=30)

     def __unicode__(self):
	return self.name
     
