from rest_framework import serializers
from .models import Notification, Signalement

class NotificationSerializer(serializers.ModelSerializer):
    user_nom = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model  = Notification
        fields = ['id', 'user', 'user_nom', 'titre', 
                  'message', 'canal', 'statut', 'created_at']
        read_only_fields = ['created_at']

from rest_framework import serializers
from .models import Notification, Signalement

class NotificationSerializer(serializers.ModelSerializer):
    user_nom = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model  = Notification
        fields = ['id', 'user', 'user_nom', 'titre',
                  'message', 'canal', 'statut', 'created_at']
        read_only_fields = ['created_at']


class SignalementSerializer(serializers.ModelSerializer):
    signaleur_nom = serializers.CharField(source='signaleur.username', read_only=True)

    class Meta:
        model  = Signalement
        fields = ['id', 'signaleur', 'signaleur_nom', 'reported_type',
                  'objet_signale_id', 'raison', 'details', 'statut',
                  'resolu_par', 'note_resolution', 'created_at']
        read_only_fields = ['created_at', 'statut', 'resolu_par']