from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)
    about = models.TextField(null=True, blank= True)
    
    def __str__(self):
        return self.name
    