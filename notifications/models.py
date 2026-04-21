from django.db import models
from users.models import Utilisateur

class Notification(models.Model):
    SMS   = 'SMS'
    PUSH  = 'PUSH'
    EMAIL = 'EMAIL'

    CANAUX = [
        (SMS,   'SMS'),
        (PUSH,  'Push'),
        (EMAIL, 'Email'),
    ]

    NON_LUE = 'NON_LUE'
    LUE     = 'LUE'

    STATUTS = [
        (NON_LUE, 'Non lue'),
        (LUE,     'Lue'),
    ]

    user       = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='notifications')
    titre      = models.CharField(max_length=200)
    message    = models.TextField()
    canal      = models.CharField(max_length=10, choices=CANAUX, default=PUSH)
    statut     = models.CharField(max_length=10, choices=STATUTS, default=NON_LUE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titre} → {self.user.username}"

class Signalement(models.Model):
    ANNONCE     = 'ANNONCE'
    UTILISATEUR = 'UTILISATEUR'
    MESSAGE     = 'MESSAGE'

    TYPES = [
        (ANNONCE,     'Annonce'),
        (UTILISATEUR, 'Utilisateur'),
        (MESSAGE,     'Message'),
    ]

    EN_ATTENTE = 'EN_ATTENTE'
    RESOLU     = 'RESOLU'
    REJETE     = 'REJETE'

    STATUTS = [
        (EN_ATTENTE, 'En attente'),
        (RESOLU,     'Résolu'),
        (REJETE,     'Rejeté'),
    ]

    signaleur          = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='signalements')
    reported_type      = models.CharField(max_length=20, choices=TYPES)
    objet_signale_id   = models.IntegerField()
    raison             = models.CharField(max_length=200)
    details            = models.TextField(blank=True)
    statut             = models.CharField(max_length=20, choices=STATUTS, default=EN_ATTENTE)
    resolu_par         = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True, blank=True, related_name='signalements_resolus')
    note_resolution    = models.TextField(blank=True)
    created_at         = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Signalement {self.reported_type} par {self.signaleur}"
