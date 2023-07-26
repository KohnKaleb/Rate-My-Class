from django.db import models
from homepage.models import Courses

# Create your models here.
class CourseRatings(models.Model):
    uuid = models.CharField(max_length=100, primary_key=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.comment