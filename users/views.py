# ✅ Code corrigé
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Utilisateur, Profil
from .serializers import UtilisateurSerializer, ProfilSerializer

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset           = Utilisateur.objects.all()
    serializer_class   = UtilisateurSerializer
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]       # s'inscrire → tout le mond
        elif self.action == 'list':
            return [permissions.IsAdminUser()]    # liste users → admin seulement
        return [permissions.IsAuthenticated()]    # reste → connecté

    @action(detail=False, methods=['get', 'put', 'patch'])
    def me(self, request):
        if request.method == 'GET':
            serializer = UtilisateurSerializer(request.user)
            return Response(serializer.data)

        serializer = UtilisateurSerializer(
            request.user,
            data=request.data,
            partial=request.method == 'PATCH'
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def change_password(self, request):
        user        = request.user
        ancien_mdp  = request.data.get('ancien_mdp')
        nouveau_mdp = request.data.get('nouveau_mdp')

        if not ancien_mdp or not nouveau_mdp:
            return Response(
                {'erreur': 'ancien_mdp et nouveau_mdp sont requis'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if not user.check_password(ancien_mdp):
            return Response(
                {'erreur': 'Ancien mot de passe incorrect'},
                status=status.HTTP_400_BAD_REQUEST
            )
        user.set_password(nouveau_mdp)
        user.save()
        return Response({'message': 'Mot de passe changé avec succès'})

    @action(detail=False, methods=['delete'])
    def delete_account(self, request):
        user = request.user
        user.delete()
        return Response({'message': 'Compte supprimé avec succès'})
    
from .models import Utilisateur, Profil
from .serializers import UtilisateurSerializer, ProfilSerializer

class ProfilViewSet(viewsets.ModelViewSet):
    queryset           = Profil.objects.all()
    serializer_class   = ProfilSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Un user voit seulement SON profil
        return Profil.objects.filter(utilisateur=self.request.user)

    def perform_create(self, serializer):
        serializer.save(utilisateur=self.request.user)