from rest_framework import serializers
from django.db import models
from users.models import Utilisateur
from messagerie.models import Message

class MessageSerializer(serializers.ModelSerializer):
    sender_nom    = serializers.CharField(source='sender.username', read_only=True)
    recipient_nom = serializers.CharField(source='recipient.username', read_only=True)

    class Meta:
        model  = Message
        fields = [
            'id', 'conversation_id', 'sender', 'sender_nom',
            'recipient', 'recipient_nom', 'listing',
            'contenu', 'is_read', 'date_lecture', 'created_at'
        ]
        read_only_fields = ['created_at', 'conversation_id']

     
