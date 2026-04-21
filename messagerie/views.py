from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset           = Message.objects.all()
    serializer_class   = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # L'expéditeur = l'utilisateur connecté
        serializer.save(sender=self.request.user)

    def get_queryset(self):
        # Un user voit seulement SES messages
        user = self.request.user
        return Message.objects.filter(
            sender=user
        ) | Message.objects.filter(
            recipient=user
        )

    @action(detail=True, methods=['post'])
    def marquer_lu(self, request, pk=None):
        message = self.get_object()
        message.is_read = True
        message.save()
        return Response({'message': 'Message marqué comme lu'})

