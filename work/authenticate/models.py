from django.db import models



class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    mark = models.FloatField()
