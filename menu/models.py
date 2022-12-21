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
    section = models.ForeignKey(menuSections, blank=True, max_length=50, on_delete=models.CASCADE, default=menuSections.objects.all().last().pk)
    description = models.TextField(max_length=350, default=None, blank=True, null=True)
    price = models.IntegerField()
    gramms = models.IntegerField(default=None, blank=True, null=True)
    calories = models.IntegerField(default=None, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    def admin_image(self):
        return '<img src="%s"/>' % self.image
    admin_image.allow_tags = True

    def __str__(self):
        return self.name

class fonts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    fontfamily = models.CharField(max_length=50)
    font = models.FileField(upload_to='menu/static/fonts/')
    def admin_image(self):
        return '<img src="%s"/>' % self.font
    admin_image.allow_tags = True

    def __str__(self):
        return self.name


class design(models.Model):
    cafename = models.CharField(max_length=50, default='cafe')
    headertxt = models.TextField(max_length=1000, default=None, blank=True, null=True)
    bgheader = models.ImageField(null=True, blank=True, upload_to='images/')
    bgup = models.ImageField(null=True, blank=True, upload_to='images/')
    bgcenter = models.ImageField(null=True, blank=True, upload_to='images/')
    bgdown = models.ImageField(null=True, blank=True, upload_to='images/')
    bgpage = models.ImageField(null=True, blank=True, upload_to='images/')
    bgend = models.ImageField(null=True, blank=True, upload_to='images/')
    font = models.ForeignKey(fonts, blank=True, max_length=50, on_delete=models.CASCADE)
    fontcolor = models.CharField(max_length=50,default=None, blank=True, null=True)
    style = models.BooleanField(default=False)

    def __str__(self):
        return self.cafename






