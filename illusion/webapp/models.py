from django.db import models

class User(models.Model):
    uuid = models.UUIDField()
    username = models.CharField(max_length=200)
    pseudo = models.CharField(max_length=200)
    party = models.JSONField()

    def __str__():
        return self.username


class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=200)
    level = models.IntegerField(default=0)

    def __str__():
        return self.character_name