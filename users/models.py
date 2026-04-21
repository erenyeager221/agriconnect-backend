from django.contrib.auth.models import AbstractUser
from django.db import models
class Utilisateur (AbstractUser):
    #Je cree des constantes pour les roles
    AGRICULTEUR = 'AGRICULTEUR'
    ACHETEUR = 'ACHETEUR'
    ADMIN = 'ADMIN'
    ROLES = [
        (AGRICULTEUR, 'Agriculteur'),  # des tuples pour les choix de roles 1-valeurs dans la base de données 2-valeurs affichées dans les formulaires
        (ACHETEUR, 'Acheteur'),
        (ADMIN, 'Admin'),
        #telephone doit etre unique pour eviter les doublons et faciliter la communication entre les utilisateurs, null et blank pour permettre aux utilisateurs de ne pas remplir ce champ s'ils ne le souhaitent pas
    ]
    telephone   = models.CharField(max_length=20, unique=True, blank=True, null=True)
    role        = models.CharField(max_length=20, choices=ROLES)
    region      = models.CharField(max_length=100, blank=True)
    est_verifie = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # pour gérer l'activation des comptes
    derniere_modification = models.DateTimeField(auto_now=True)  # pour suivre les modifications du compte
    official_homepage = models.URLField(blank=True, null=True)  # pour les agriculteurs qui ont une page officielle

    def __str__(self):
        return f"{self.username}"

class Profil(models.Model):
    utilisateur       = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='profil')
    nom_complet       = models.CharField(max_length=200, blank=True)
    region            = models.CharField(max_length=100, blank=True)
    departement       = models.CharField(max_length=100, blank=True)
    commune           = models.CharField(max_length=100, blank=True)
    adresse_complete  = models.TextField(blank=True)
    latitude          = models.FloatField(null=True, blank=True)
    longitude         = models.FloatField(null=True, blank=True)
    note_moyenne      = models.FloatField(default=0.0)
    nb_transactions   = models.IntegerField(default=0)
    created_at        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profil de {self.utilisateur.username}"
#je creer un super utilisateur pour le role admin
#python manage.py createsuperuser --username admin --email
