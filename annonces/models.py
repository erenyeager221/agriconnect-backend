from django.db import models
from users.models import Utilisateur

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    unite_de_mesure = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.nom

class Annonce(models.Model):
    status = [
        ('DISPONIBLE', 'Disponible'),
        ('VENDU', 'Vendu'),
        ('EXPIRÉ', 'Expiré'),
        ('RÉSERVÉ', 'Réservé')
    ]
   
    titre = models.CharField(max_length=150)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    description = models.TextField()
    prix= models.DecimalField(max_digits=10, decimal_places=2)
    date_de_recolte = models.DateField()
    quantite_disponible = models.DecimalField(max_digits=10, decimal_places=2)
    fait_par = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_de_publication = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=30, choices=status, default='DISPONIBLE')
   
    def __str__(self):
        return f"{self.titre}, {self.description},{self.prix} CFA"


class AnnonceFavorite(models.Model):
    user       = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='favoris')
    annonce    = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='favoris')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'annonce']  # un user ne peut pas ajouter 2x la même annonce

    def __str__(self):
        return f"{self.user.username} ❤️ {self.annonce.titre}"
    

class Recherche(models.Model):
    user              = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='recherches')
    nom_recherche     = models.CharField(max_length=200)
    criteres          = models.JSONField(default=dict)
    alertes_actives   = models.BooleanField(default=False)
    created_at        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} — {self.nom_recherche}"
    

class PrixMarche(models.Model):
    categorie   = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='prix_marche')
    region      = models.CharField(max_length=100)
    prix_moyen  = models.DecimalField(max_digits=10, decimal_places=2)
    prix_minimum = models.DecimalField(max_digits=10, decimal_places=2)
    prix_maximum = models.DecimalField(max_digits=10, decimal_places=2)
    date_calcul = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.categorie.nom} — {self.region} — {self.prix_moyen} FCFA"
    

class ImageProduit(models.Model):
    annonce         = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='images')
    image_url       = models.URLField()
    url_miniature   = models.URLField(blank=True)
    ordre_affichage = models.IntegerField(default=0)
    mise_a_jour     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image {self.ordre_affichage} — {self.annonce.titre}"