import random
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
''' 
Where user data will be stored at hear 
'''
class Userprofile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    average_cycle_length = models.IntegerField(default=28)
    average_period_length = models.IntegerField(default=5)
    last_period_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
        
class User(AbstractUser):
    opt = models.CharField(max_length=6 , blank=True , null=True)
    
    
    def generate_opt(self):
        opt_code = str(random.randint(10000 , 999999))
        self.opt = opt_code
        self.save()
        return opt_code