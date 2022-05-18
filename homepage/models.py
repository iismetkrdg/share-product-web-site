from django.db import models
from django.contrib.auth.models import User


class Alici(models.Model):
   name = models.CharField(max_length=50)
   def __str__(self):
      return self.name
class Urun(models.Model):
   author = models.CharField(max_length=35)
   content= models.TextField()
   img = models.ImageField(upload_to='images/')
   tl = models.CharField(max_length=16)
   alici=models.CharField(max_length=50)
   created_at = models.DateTimeField(auto_now_add=True,null=True)   
   class Meta:
      ordering = ['-created_at']
   def __str__(self):
      return self.author