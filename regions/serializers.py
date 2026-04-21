from rest_framework import serializers
from .models import Region

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Region
        fields = ['id', 'nom_region', 'code_region', 'latitude', 'longitude']