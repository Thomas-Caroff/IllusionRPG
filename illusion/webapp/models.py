from django.db import models
import utils.customUUID as guid

class GUIDModel(models.Model):
    id = models.CharField(primary_key=True, max_length=32, default=guid.custom_id)

class User(GUIDModel):
    ##Infos
    username = models.CharField(max_length=200, unique=True)
    pseudo = models.CharField(default="", blank=True, max_length=200, unique=True)
    party_list = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.username


class Campaign(GUIDModel):
    campaign_name = models.CharField(default="", max_length=100, unique=True)
    description = models.CharField(blank=True, default="", max_length=5000)


class Party(GUIDModel):
    party_name = models.CharField(default="", max_length=100)
    quadgram = models.CharField(default="", max_length=4, unique=True)
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE)


class Character(GUIDModel):
    ##Global
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    character_name = models.CharField(default="", max_length=200)
    description = models.CharField(blank=True, default="", max_length=5000)
    party_id = models.ForeignKey(Party, null=True, blank=True, on_delete=models.SET_NULL)

    ##Accessories
    items = models.CharField(blank=True, default="", max_length=500)
    level = models.IntegerField(default=0)

    ##Stats
    strength = models.IntegerField(default=10)
    agility = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    diplomacy = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)

    def __str__(self):
        return self.character_name