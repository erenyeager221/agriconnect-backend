from annonces.models import Annonce, Categorie, AnnonceFavorite, Recherche, PrixMarche, ImageProduit
from annonces.serializers import AnnonceSerializer, CategorieSerializer, AnnonceFavoriteSerializer, RechercheSerializer, PrixMarcheSerializer, ImageProduitSerializer
from rest_framework import viewsets, permissions


class CategorieViewSet(viewsets.ModelViewSet):
    queryset           = Categorie.objects.all()
    serializer_class   = CategorieSerializer
    permission_classes = [permissions.AllowAny]


class AnnonceViewSet(viewsets.ModelViewSet):
    queryset           = Annonce.objects.all()
    serializer_class   = AnnonceSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        region = self.request.query_params.get('region')
        if region:
            return Annonce.objects.filter(region=region)
        return Annonce.objects.all()
    


class AnnonceFavoriteViewSet(viewsets.ModelViewSet):
    queryset           = AnnonceFavorite.objects.all()
    serializer_class   = AnnonceFavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AnnonceFavorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class RechercheViewSet(viewsets.ModelViewSet):
    queryset           = Recherche.objects.all()
    serializer_class   = RechercheSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Recherche.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)






class PrixMarcheViewSet(viewsets.ModelViewSet):
    queryset           = PrixMarche.objects.all()
    serializer_class   = PrixMarcheSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        region = self.request.query_params.get('region')
        categorie = self.request.query_params.get('categorie')
        queryset = PrixMarche.objects.all()
        if region:
            queryset = queryset.filter(region=region)
        if categorie:
            queryset = queryset.filter(categorie=categorie)
        return queryset
    


class ImageProduitViewSet(viewsets.ModelViewSet):
    queryset           = ImageProduit.objects.all()
    serializer_class   = ImageProduitSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        annonce_id = self.request.query_params.get('annonce')
        if annonce_id:
            return ImageProduit.objects.filter(annonce=annonce_id)
        return ImageProduit.objects.all()