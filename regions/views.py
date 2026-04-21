from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Region
from .serializers import RegionSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset           = Region.objects.all()
    serializer_class   = RegionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

