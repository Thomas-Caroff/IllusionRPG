from django.db import models
import utils.customUUID as guid

class GUIDModel(models.Model):
    id = models.CharField(primary_key=True, max_length=32)

class User(GUIDModel):
    ##Infos
    username = models.CharField(max_length=200)
    pseudo = models.CharField(max_length=200)
    party_list = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Character(GUIDModel):
    ##Global
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    character_name = models.CharField(default="", max_length=200)
    level = models.IntegerField(default=0)
    description = models.CharField(default="", max_length=5000)

    ##Accessories
    items = models.CharField(default="", max_length=500)

    ##Stats
    strength = models.IntegerField(default=10)
    agility = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    diplomacy = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)

    def __str__(self):
        return self.character_name



class Campaign(GUIDModel):
    campaign_name = models.CharField(default="", max_length=100)
    description = models.CharField(default="", max_length=5000)


class Party(GUIDModel):
    party_name = models.CharField(default="", max_length=100)
    quadgram = models.CharField(default="", max_length=4)
    party_character = models.CharField(default="", max_length=200)
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE)
