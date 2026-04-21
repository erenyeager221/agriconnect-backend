from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Transaction, Evaluation
from .serializers import TransactionSerializer, EvaluationSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset           = Transaction.objects.all()
    serializer_class   = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Un user voit seulement SES transactions
        user = self.request.user
        return Transaction.objects.filter(
            Q(buyer=user) | Q(seller=user)
        )

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

    @action(detail=True, methods=['post'])
    def confirmer(self, request, pk=None):
        transaction = self.get_object()
        if transaction.seller != request.user:
            return Response(
                {'erreur': 'Seul le vendeur peut confirmer'},
                status=status.HTTP_403_FORBIDDEN
            )
        transaction.statut = 'CONFIRMEE'
        transaction.save()
        return Response({'message': 'Transaction confirmée ✅'})

    @action(detail=True, methods=['post'])
    def annuler(self, request, pk=None):
        transaction = self.get_object()
        raison = request.data.get('raison', '')
        transaction.statut = 'ANNULEE'
        transaction.save()
        return Response({'message': f'Transaction annulée — {raison}'})

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset           = Evaluation.objects.all()
    serializer_class   = EvaluationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Evaluation.objects.filter(reviewer=user) |\
               Evaluation.objects.filter(reviewed=user)

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)

    @action(detail=True, methods=['post'])
    def approuver(self, request, pk=None):
        evaluation = self.get_object()
        evaluation.est_approuve = True
        evaluation.save()
        return Response({'message': 'Évaluation approuvée ✅'})