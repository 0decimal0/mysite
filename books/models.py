from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    website = models.URLField()
    def __str__(self):
        return '%s %s %s' %(self.name,self.address,self.country)
    class Admin:
        pass

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return '%s %s' %(self.first_name,self.last_name)
    class Admin:
        pass

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)    
    publication_date = models.DateField()
    def __str__(self):
        return self.title
    class Admin:
        pass
