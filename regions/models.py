from django.db import models

class Region(models.Model):
    nom_region = models.CharField(max_length=200)
    code_region = models.CharField(max_length=10, unique=True)
    latitude    = models.FloatField(null=True, blank=True)
    longitude   = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nom_region