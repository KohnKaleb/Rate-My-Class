from django.db import models

# Create your models here.
class Courses(models.Model):
    uuid = models.CharField(max_length=100, primary_key=True)
    number = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
