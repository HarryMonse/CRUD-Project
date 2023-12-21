from django.db import models


# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=25,blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    password = models.CharField(max_length=25,blank=False,null=False)

    def __str__(self):
        return self.username
