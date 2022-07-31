from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")