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
    description = models.TextField(blank=True, default="", max_length=5000)

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

class CharacterClass(GUIDModel):
    class_name = models.CharField(default="Commoner", max_length=200)
    base_system = models.ForeignKey(BaseSystem, null=True, blank=True, on_delete=models.SET_NULL)
    is_homebrew = models.BooleanField(default=False)
    hp_dice = models.IntegerField(null=True, default=6)
    
    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(null=True, default=10)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    diplomacy = models.IntegerField(null=True, default=None)

class CharacterRace(GUIDModel):
    race_name = models.CharField(default="", max_length=200)
    base_system = models.ForeignKey(BaseSystem, null=True, blank=True, on_delete=models.SET_NULL)
    is_homebrew = models.BooleanField(default=False)

    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(null=True, default=10)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    diplomacy = models.IntegerField(null=True, default=None)

class Aptitude(GUIDModel):
    is_from_class = models.BooleanField(default=False)
    is_from_race = models.BooleanField(default=True)
    is_homebrew = models.BooleanField(default=False)
    aptitude_name = models.CharField(default="", max_length=200)
    description = models.TextField(blank=True, default="", max_length=5000)

class Spell(GUIDModel):
    spell_name = models.CharField(default="", max_length=200)
    damages = models.IntegerField(null=True, default=0)
    level = models.IntegerField(blank=True, default=0)
    property = models.CharField(blank=True, default="", max_length=500)
    is_bonus_action = models.BooleanField(default=False)
    is_homebrew = models.BooleanField(default=False)

class Weapon(GUIDModel):
    weapon_name = models.CharField(default="", max_length=200)
    damages = models.IntegerField(default=4)
    is_damaged = models.BooleanField(default=False)
    price = models.IntegerField(default=0) #price in copper coins
    damage_type = models.CharField(blank=True, default="", max_length=100)
    properties = models.CharField(blank=True, default="", max_length=500)
    ammo = models.IntegerField(blank = True, default=0)

class Armor(GUIDModel):
    armor_name = models.CharField(default="", max_length=200)
    ca = models.IntegerField(default=11)
    is_damaged = models.BooleanField(default=False)
    price = models.IntegerField(default=0) #price in copper coins
    max_dex_modifier = models.IntegerField(default=2)
    required_force = models.IntegerField(default=0)
    disadvantage_stealth = models.BooleanField(default=False)
    disadvantage_athletism = models.BooleanField(default=False)

class Items(GUIDModel):
    item_name = models.CharField(default="", max_length=200)
    price = models.IntegerField(default=0) #price in copper coins
    is_homebrew = models.BooleanField(default=False)

class Character(GUIDModel):
    ##Global
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    character_name = models.CharField(default="", max_length=200)
    description = models.TextField(blank=True, default="", max_length=5000)
    character_class_id = models.ForeignKey(CharacterClass, null=True, blank=True, on_delete=models.SET_NULL)
    character_race_id = models.ForeignKey(CharacterRace, null=True, blank=True, on_delete=models.SET_NULL)
    party_id = models.ForeignKey(Party, null=True, blank=True, on_delete=models.SET_NULL)

    ##Money
    copper_coins = models.IntegerField(default=0)
    silver_coins = models.IntegerField(default=0)
    gold_coins = models.IntegerField(default=0)
    platinum_coins = models.IntegerField(default=0)

    ##Stats
    level = models.IntegerField(default=0)
    proficiency_bonus = models.IntegerField(default=2)

    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(null=True, default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    diplomacy = models.IntegerField(null=True, default=None)

    def __str__(self):
        return self.character_name

class CharacterWeapon(GUIDModel):
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    weapon_type = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    nickname = models.CharField(blank=True, default="", max_length=100)
    is_equipped = models.BooleanField(default=False)
    ammo_count = models.IntegerField(blank = True, default=0)

class CharacterArmor(GUIDModel):
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    weapon_type = models.ForeignKey(Armor, on_delete=models.CASCADE)
    nickname = models.CharField(blank=True, default="", max_length=100)
    is_equipped = models.BooleanField(default=False)

class CharacterItems(GUIDModel):
    character_id = models.ForeignKey(Character, null=True, blank=True, on_delete=models.SET_NULL)
    item_id = models.ForeignKey(Items, null=True, blank=True, on_delete=models.SET_NULL)
    nickname = models.CharField(blank=True, default="", max_length=100)
    is_item_hidden = models.BooleanField(default=False)