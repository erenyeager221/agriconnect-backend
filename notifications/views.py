from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Notification, Signalement
from .serializers import NotificationSerializer, SignalementSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset           = Notification.objects.all()
    serializer_class   = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Un user voit seulement SES notifications
        return Notification.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def marquer_lue(self, request, pk=None):
        notification = self.get_object()
        notification.statut = 'LUE'
        notification.save()
        return Response({'message': 'Notification marquée comme lue ✅'})

    @action(detail=False, methods=['post'])
    def tout_marquer_lue(self, request):
        Notification.objects.filter(
            user=request.user, statut='NON_LUE'
        ).update(statut='LUE')
        return Response({'message': 'Toutes les notifications marquées comme lues ✅'})
    

class SignalementViewSet(viewsets.ModelViewSet):
    queryset           = Signalement.objects.all()
    serializer_class   = SignalementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Signalement.objects.filter(signaleur=self.request.user)

    def perform_create(self, serializer):
        serializer.save(signaleur=self.request.user)

    @action(detail=True, methods=['post'])
    def resoudre(self, request, pk=None):
        signalement = self.get_object()
        note = request.data.get('note_resolution', '')
        signalement.statut       = 'RESOLU'
        signalement.resolu_par   = request.user
        signalement.note_resolution = note
        signalement.save()
        return Response({'message': 'Signalement résolu ✅'})