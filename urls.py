from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UtilisateurViewSet, ProfilViewSet
from annonces.views import AnnonceViewSet, CategorieViewSet, AnnonceFavoriteViewSet, RechercheViewSet, PrixMarcheViewSet, ImageProduitViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView
from messagerie.views import MessageViewSet
from transactions.views import TransactionViewSet
from notifications.views import NotificationViewSet, SignalementViewSet
from regions.views import RegionViewSet


router = DefaultRouter()
router.register('users', UtilisateurViewSet)
router.register('annonces', AnnonceViewSet)
router.register('categories', CategorieViewSet)
router.register('messages', MessageViewSet)
router.register('transactions', TransactionViewSet)
router.register('notifications', NotificationViewSet)
router.register('profils', ProfilViewSet)
router.register('signalements', SignalementViewSet)
router.register('favoris', AnnonceFavoriteViewSet)
router.register('recherches', RechercheViewSet)
router.register('prix-marche', PrixMarcheViewSet)
router.register('regions', RegionViewSet)
router.register('images', ImageProduitViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/login/',   TokenObtainPairView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),
    path('api/auth/logout/', TokenBlacklistView.as_view())
  
    ]