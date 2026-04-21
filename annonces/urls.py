from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategorieViewSet, AnnonceViewSet  

router = DefaultRouter()
router.register('categories', CategorieViewSet )  # à toi de compléter
router.register('annonces', AnnonceViewSet)  # à toi de compléter

urlpatterns = [
    path('', include(router.urls)),
]