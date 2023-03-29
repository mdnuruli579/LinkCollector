from django.db import models

# Create your models here.
from django.db import models
 
# Create your models here.
class Link(models.Model):
 
    def __str__(self):
        return self.name
 
    address = models.CharField(max_length=1000,null=True,blank=True)
    name = models.CharField(max_length=1000,null=True,blank=True)
    author=models.CharField(max_length=100,null=True,blank=True)
    date=models.CharField(max_length=20,null=True,blank=True)

