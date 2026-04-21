from rest_framework import serializers
from .models import Utilisateur, Profil

class UtilisateurSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Utilisateur # on spécifie le modèle à utiliser pour ce serializer, ici c'est le modèle User que nous avons défini dans models.py
        fields = ['id', 'username', 'email', 'password',
                  'telephone', 'role', 'region', 'est_verifie', 'created_at']

    def create(self, validated_data): #validated_data contient les données validées par le serializer, c'est un dictionnaire qui contient les champs et leurs valeurs
        password = validated_data.pop('password') # on retire le mot de passe des données validées pour le traiter séparément
        user = Utilisateur(**validated_data) # on crée une instance de l'utilisateur avec les autres données validées
        user.set_password(password) # on utilise la méthode set_password pour hasher le mot de passe avant de le sauvegarder dans la base de données
        user.save() # on sauvegarde l'utilisateur dans la base de données
        return user 
    
class ProfilSerializer(serializers.ModelSerializer):
    utilisateur_nom = serializers.CharField(
        source='utilisateur.username', 
        read_only=True
    )

    class Meta:
        model  = Profil
        fields = ['id', 'utilisateur', 'utilisateur_nom', 'nom_complet',
                  'region', 'departement', 'commune', 'adresse_complete',
                  'latitude', 'longitude', 'note_moyenne', 'nb_transactions',
                  'created_at']
        read_only_fields = ['created_at', 'note_moyenne', 'nb_transactions']