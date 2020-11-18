from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=50)
    USN = models.CharField(max_length=10, primary_key=True)
    Branch = models.CharField(max_length=3)

    def __str__(self):
        return self.USN