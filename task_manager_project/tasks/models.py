from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'tasks')
    
    PRIORITY_CHOICES = (
        ('L','Low'),
        ('M','Medium'),
        ('H','High'),
    )

    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    completed = models.BooleanField(default = False)
    priority = models.CharField(max_length = 1,choices = PRIORITY_CHOICES,default = 'L')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title