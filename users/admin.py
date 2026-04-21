from django.contrib import admin
from users.models import Utilisateur, Profil
@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display   = ['username', 'email', 'role', 'est_verifie', 'created_at']
    list_filter    = ['role', 'est_verifie']
    search_fields  = ['username', 'email', 'telephone']

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display   = ['utilisateur', 'nom_complet', 'region', 'note_moyenne']
    search_fields  = ['nom_complet', 'region']