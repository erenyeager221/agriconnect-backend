from rest_framework import serializers
from annonces.models import Annonce, Categorie, AnnonceFavorite, Recherche, PrixMarche, ImageProduit
from users.models import Utilisateur

class AnnonceSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Annonce
        fields = ['id', 'titre', 'description', 'categorie',
                  'prix', 'quantite_disponible', 'date_de_recolte',
                  'statut', 'date_de_publication','fait_par' ]
        read_only_fields = ['date_publication'] # on rend ces champs en lecture seule car ils seront automatiquement définis lors de la création d'une annonc
        def create(self, validated_data):
            return Annonce.objects.create(**validated_data)
    

class CategorieSerializer(serializers.ModelSerializer):
        class Meta:
          model = Categorie
          fields = ['nom','description']
        def create(self,validated_data): 
             return Categorie.objects.create( **validated_data)
        


class AnnonceFavoriteSerializer(serializers.ModelSerializer):
    annonce_titre = serializers.CharField(source='annonce.titre', read_only=True)
    user_nom      = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model  = AnnonceFavorite
        fields = ['id', 'user', 'user_nom', 'annonce', 'annonce_titre', 'created_at']
        read_only_fields = ['created_at']



class RechercheSerializer(serializers.ModelSerializer):
    user_nom = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model  = Recherche
        fields = ['id', 'user', 'user_nom', 'nom_recherche',
                  'criteres', 'alertes_actives', 'created_at']
        read_only_fields = ['created_at']

  

class PrixMarcheSerializer(serializers.ModelSerializer):
    categorie_nom = serializers.CharField(source='categorie.nom', read_only=True)

    class Meta:
        model  = PrixMarche
        fields = ['id', 'categorie', 'categorie_nom', 'region',
                  'prix_moyen', 'prix_minimum', 'prix_maximum', 'date_calcul']
        read_only_fields = ['date_calcul']




class ImageProduitSerializer(serializers.ModelSerializer):
    annonce_titre = serializers.CharField(source='annonce.titre', read_only=True)

    class Meta:
        model  = ImageProduit
        fields = ['id', 'annonce', 'annonce_titre', 'image_url',
                  'url_miniature', 'ordre_affichage', 'mise_a_jour']
        read_only_fields = ['mise_a_jour']