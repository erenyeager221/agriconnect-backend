from django.contrib import admin
from .models import Annonce, Categorie, AnnonceFavorite, Recherche, PrixMarche, ImageProduit

admin.site.register(Annonce)
admin.site.register(Categorie)
admin.site.register(AnnonceFavorite)
admin.site.register(Recherche)
admin.site.register(PrixMarche)
admin.site.register(ImageProduit)
