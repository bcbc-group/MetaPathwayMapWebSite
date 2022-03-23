# Create your models here.
from django.db import models

class mpmUpload(models.Model):
    ORGANISM = [
    ('PlantCyc', 'PlantCyc'),
    ('BrachyCyc', 'BrachyCyc'),
    ('SolCyc', 'SolCyc'),
 ]

    organism = models.CharField(max_length=10, choices=ORGANISM)
    canopus_predictions = models.FileField(upload_to="static/tmp", null=True, blank=True)
