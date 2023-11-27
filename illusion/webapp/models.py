from django.db import models
import uuid

class GUIDModel(models.Model):
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class User(GUIDModel):
    username = models.CharField(max_length=200)
    pseudo = models.CharField(max_length=200)
    party = models.JSONField()

    def __str__(self):
        return self.username


class Character(GUIDModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=200)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.character_name