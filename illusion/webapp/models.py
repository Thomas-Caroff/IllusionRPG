from django.db import models
import utils.customUUID as guid

class GUIDModel(models.Model):
    id = models.CharField(primary_key=True, max_length=32, default=guid.custom_id)

class BaseSystem(GUIDModel):
    system_name = models.CharField(default="", max_length=200)
    url = models.CharField(default="", null=True, blank=True, max_length=5000)

class User(GUIDModel):
    ##Infos
    username = models.CharField(max_length=200, unique=True)
    pseudo = models.CharField(default="", blank=True, max_length=200, unique=True)
    party_list = models.CharField(blank=True, max_length=200)

    def __str__(self) -> str:
        return self.username


class Campaign(GUIDModel):
    campaign_name = models.CharField(default="", max_length=100, unique=True)
    quadgram = models.CharField(default="", max_length=4, unique=True)
    base_system_id = models.ForeignKey(BaseSystem, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.CharField(blank=True, default="", max_length=5000)

    def __str__(self) -> str:
        return self.campaign_name


class Party(GUIDModel):
    party_name = models.CharField(default="", max_length=100)
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.party_name


class DM(GUIDModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    party_id = models.ForeignKey(Party, on_delete=models.CASCADE)


class Character_Class(GUIDModel):
    class_name = models.CharField(default="Commoner", max_length=200)
    base_system = models.ForeignKey(BaseSystem, null=True, blank=True, on_delete=models.SET_NULL)
    is_homebrew = models.BooleanField(default=False)
    
    strength = models.IntegerField(default=0)
    agility = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    diplomacy = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)

class Character_Race(GUIDModel):
    race_name = models.CharField(default="", max_length=200)
    base_system = models.ForeignKey(BaseSystem, null=True, blank=True, on_delete=models.SET_NULL)
    is_homebrew = models.BooleanField(default=False)

    strength = models.IntegerField(default=0)
    agility = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0) 
    diplomacy = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)

class Character(GUIDModel):
    ##Global
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    character_name = models.CharField(default="", max_length=200)
    description = models.CharField(blank=True, default="", max_length=5000)
    character_class_id = models.ForeignKey(Character_Class, null=True, blank=True, on_delete=models.SET_NULL)
    character_race_id = models.ForeignKey(Character_Race, null=True, blank=True, on_delete=models.SET_NULL)
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