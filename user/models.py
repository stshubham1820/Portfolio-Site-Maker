from django.db import models

# Create your models here.
class User(models.Model):
    UserName = models.CharField(max_length=50,primary_key=True)
    Password = models.CharField(max_length=50)
    Email = models.EmailField(max_length = 254)