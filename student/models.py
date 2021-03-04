from django.db import models

# Create your models here.

class student(models.Model):
    roll_no = models.CharField(max_length=20,unique=True,primary_key=True)
    name = models.CharField(max_length=60)
    marks_maths = models.PositiveIntegerField()
    marks_physics = models.PositiveIntegerField()
    marks_chemistry = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    percentage = models.FloatField()

    def __str__(self):
        return self.roll_no


