from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UtilisateurViewSet, ProfilViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Le router crée automatiquement toutes les URLs
router = DefaultRouter()
router.register('users', UtilisateurViewSet)
router.register('profils', ProfilViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
