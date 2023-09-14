from django.db import models

class RiverData(models.Model):
    float_number = models.IntegerField()
    float_date = models.DateField()
    floated_status = models.BooleanField()