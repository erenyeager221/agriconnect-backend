from rest_framework import serializers
from .models import Transaction, Evaluation

class TransactionSerializer(serializers.ModelSerializer):
    buyer_nom  = serializers.CharField(source='buyer.username', read_only=True)
    seller_nom = serializers.CharField(source='seller.username', read_only=True)
    listing_titre = serializers.CharField(source='listing.titre', read_only=True)
    class Meta:
        model  = Transaction
        fields = [
            'id', 'listing', 'listing_titre',
            'buyer', 'buyer_nom',
            'seller', 'seller_nom',
            'quantite_achetee', 'prix_unitaire', 'montant_total',
            'statut', 'complete_le', 'created_at'
        ]
        read_only_fields = ['created_at', 'montant_total']

    def create(self, validated_data):
        # Calculer automatiquement le montant total
        quantite = validated_data.get('quantite_achetee', 0)
        prix     = validated_data.get('prix_unitaire', 0)
        validated_data['montant_total'] = quantite * prix
        return Transaction.objects.create(**validated_data)



class EvaluationSerializer(serializers.ModelSerializer):
    reviewer_nom = serializers.CharField(source='reviewer.username', read_only=True)
    reviewed_nom = serializers.CharField(source='reviewed.username', read_only=True)

    class Meta:
        model  = Evaluation
        fields = ['id', 'reviewer', 'reviewer_nom', 'reviewed', 'reviewed_nom',
                  'listing', 'note_globale', 'commentaire', 'note_qualite',
                  'note_quantite', 'note_ponctualite', 'note_communication',
                  'est_approuve', 'created_at']
        read_only_fields = ['created_at', 'est_approuve']