from django.db import models
from users.models import Utilisateur
from annonces.models import Annonce

class Transaction(models.Model):
    # Statuts possibles
    EN_ATTENTE = 'EN_ATTENTE'
    CONFIRMEE  = 'CONFIRMEE'
    LIVREE     = 'LIVREE'
    ANNULEE    = 'ANNULEE'

    STATUTS = [
        (EN_ATTENTE, 'En attente'),
        (CONFIRMEE,  'Confirmée'),
        (LIVREE,     'Livrée'),
        (ANNULEE,    'Annulée'),
    ]

    listing          = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    buyer            = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='achats')
    seller           = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='ventes')
    quantite_achetee = models.FloatField()
    prix_unitaire    = models.FloatField()
    montant_total    = models.FloatField()
    statut           = models.CharField(max_length=20, choices=STATUTS, default=EN_ATTENTE)
    complete_le      = models.DateTimeField(null=True, blank=True)
    created_at       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} — {self.buyer} → {self.seller}"


class Evaluation(models.Model):
    reviewer        = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='evaluations_donnees')
    reviewed        = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='evaluations_recues')
    listing         = models.ForeignKey(Annonce, on_delete=models.CASCADE, null=True, blank=True)
    note_globale    = models.IntegerField()
    commentaire     = models.TextField(blank=True)
    note_qualite    = models.IntegerField()
    note_quantite   = models.IntegerField()
    note_ponctualite = models.IntegerField()
    note_communication = models.IntegerField()
    est_approuve    = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer} → {self.reviewed} ({self.note_globale}/5)"