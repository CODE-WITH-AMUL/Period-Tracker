from django.db import models
from django.contrib.auth.models import User

'''
Creating the datebase for the cycle of period where its stared and when it ends
'''

class Cycle(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True , auto_now_add=True)
    symptom = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Cycle for {self.user.username}"
    

class PeiodEntry(models.Model):
    date = models.DateTimeField(unique=True)
    notes = models.TextField(blank=True)
    def __str__(self):
        return f"Period on {self.date}"


class Note(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"The note of {self.user} - {self.notes[:20]}"
    