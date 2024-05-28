from django.db import models

class RiverData(models.Model):
    FLOAT_STATUS_CHOICES = [
        ('N', 'No'),
        ('Y', 'Yes'),
        ('S', 'Skipped'),
    ]

    float_number = models.IntegerField()
    float_date = models.DateField()
    floated_status = models.CharField(max_length=1, choices=FLOAT_STATUS_CHOICES)
