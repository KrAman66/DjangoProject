from django.db import models

class addition(models.Model):
    name = models.CharField(max_length=20)
    input1 = models.IntegerField()
    input2 = models.IntegerField()
    sum_val = models.IntegerField()
