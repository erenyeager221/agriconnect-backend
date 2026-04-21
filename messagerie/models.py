from django.db import models
import uuid
from users.models import Utilisateur
from annonces.models import Annonce

class Message(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation_id = models.UUIDField(default=uuid.uuid4)
    sender          = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_envoyes')
    recipient       = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_recus')
    listing         = models.ForeignKey(Annonce, on_delete=models.SET_NULL, null=True, blank=True)
    contenu         = models.TextField()
    is_read         = models.BooleanField(default=False)
    date_lecture    = models.DateTimeField(null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} → {self.recipient}"

    def marquer_comme_lu(self):
        self.is_read = True
        self.save()