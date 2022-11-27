from cgi import print_exception
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User


class menuSections(models.Model):
    id = models.AutoField(primary_key=True)
    section = models.CharField(max_length=50)
 
    def __str__(self):
        return self.section


class items(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    section = models.ForeignKey(menuSections, blank=True, max_length=50, on_delete=models.CASCADE)
    description = models.TextField(max_length=350, default=None, blank=True, null=True)
    price = models.IntegerField()
    gramms = models.IntegerField(default=None, blank=True, null=True)
    calories = models.IntegerField(default=None, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name
