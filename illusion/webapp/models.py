from django.db import models
import utils.customUUID as guid

class GUIDModel(models.Model):
    id = models.CharField(primary_key=True, max_length=32, default=guid.custom_id)

#region BaseSystem
class BaseSystem(GUIDModel):
    system_name = models.CharField(default="", max_length=200)
    url = models.CharField(default="", null=True, blank=True, max_length=5000)

    def __str__(self) -> str:
        return self.system_name
#endregion

#region User
class User(GUIDModel):
    ##Infos
    username = models.CharField(max_length=200, unique=True)
    pseudo = models.CharField(default="", blank=True, max_length=200, unique=True)
    party_list = models.CharField(blank=True, max_length=200)

    def __str__(self) -> str:
        return self.username
#endregion

#region Campaign
class Campaign(GUIDModel):
    campaign_name = models.CharField(default="", max_length=100, unique=True)
    quadgram = models.CharField(default="", max_length=4, unique=True)
    base_system_id = models.ForeignKey(BaseSystem, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, default="", max_length=5000)

    def __str__(self) -> str:
        return self.campaign_name
#endregion

#region Party
class Party(GUIDModel):
    party_name = models.CharField(default="", max_length=100)
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.party_name
#endregion

#region DM
class DM(GUIDModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    party_id = models.ForeignKey(Party, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"DM: {self.user_id.username} | Party: {self.party_id.party_name}"
#endregion

#region Character Stat
class CharacterStats(GUIDModel):
    #DnD/FF/PF
    strength = models.IntegerField(null=True, default=10)
    str_mod = models.IntegerField(null=True, default=0)
    dexterity = models.IntegerField(null=True, default=10)
    dex_mod = models.IntegerField(null=True, default=0)
    constitution = models.IntegerField(null=True, default=10)
    con_mod = models.IntegerField(null=True, default=0)
    intelligence = models.IntegerField(null=True, default=10)
    int_mod = models.IntegerField(null=True, default=0)
    wisdom = models.IntegerField(null=True, default=10)
    wis_mod = models.IntegerField(null=True, default=0)
    charisma = models.IntegerField(null=True, default=10)
    cha_mod = models.IntegerField(null=True, default=0)

    #Illusion
    diplomacy = models.IntegerField(null=True, blank=True, default=None)
    dip_mod = models.IntegerField(null=True, blank=True, default=None)

    #Aventure
    physic = models.IntegerField(null=True, blank=True, default=None)
    social = models.IntegerField(null=True, blank=True, default=None)
    mental = models.IntegerField(null=True, blank=True, default=None)

    #Skill Expertise
    proficiency_bonus = models.IntegerField(default=2)
    skill_proficiency = models.TextField(null=True, blank=True, default="", max_length=640)
    skill_expertise = models.TextField(null=True, blank=True, default="", max_length=640)
#endregion

#region Character Class
class CharacterClass(GUIDModel):
    class_name = models.CharField(default="Commoner", max_length=200)
    base_system = models.ForeignKey(BaseSystem, null=True, blank=True, on_delete=models.SET_NULL)
    is_homebrew = models.BooleanField(default=False)
    hp_dice = models.IntegerField(null=True, default=6)
    
    bonus_stats = models.ForeignKey(CharacterStats, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f"{self.class_name} | {self.base_system}"
#endregion

#region Character Species
class CharacterSpecies(GUIDModel):
    species_name = models.CharField(default="", max_length=200)
    base_system = models.ForeignKey(BaseSystem, null=True, blank=True, on_delete=models.SET_NULL)
    is_homebrew = models.BooleanField(default=False)

    bonus_stats = models.ForeignKey(CharacterStats, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f"{self.species_name} | {self.base_system}"
#endregion

#region Skill
class Skill(GUIDModel):
    skill_name = models.CharField(default="", max_length=50)
    is_saving_throw = models.BooleanField(default=False)
    modified_by = models.CharField(default="", null=True, blank=True, max_length=20)

    def __str__(self) -> str:
        return f"{self.skill_name}"
#endregion

#region Skill Set
class SkillSet(GUIDModel):
    base_system_id = models.ForeignKey(BaseSystem, null=True, blank=True, on_delete=models.CASCADE)
    skill_set_name = models.CharField(default="", max_length=200)
    skill_list = models.TextField(default="", max_length=640)

    def __str__(self) -> str:
        return f"{self.skill_set_name} ({self.base_system_id})"
#endregion

#region Aptitude
class Aptitude(GUIDModel):
    is_from_class = models.BooleanField(default=False)
    is_from_species = models.BooleanField(default=True)
    is_homebrew = models.BooleanField(default=False)
    aptitude_name = models.CharField(default="", max_length=200)
    description = models.TextField(blank=True, default="", max_length=5000)

    def __str__(self) -> str:
        return self.aptitude_name
#endregion

#region Spell
class Spell(GUIDModel):
    spell_name = models.CharField(default="", max_length=200)
    damages = models.IntegerField(null=True, default=0)
    level = models.IntegerField(blank=True, default=0)
    property = models.CharField(blank=True, default="", max_length=500)
    is_bonus_action = models.BooleanField(default=False)
    is_homebrew = models.BooleanField(default=False)
    class_limit = models.CharField(default="", null=True, blank=True, max_length=320)

    def __str__(self) -> str:
        return self.spell_name
#endregion

#region Weapon
class Weapon(GUIDModel):
    weapon_name = models.CharField(default="", max_length=200)
    damages = models.IntegerField(default=4)
    is_damaged = models.BooleanField(default=False)
    price = models.IntegerField(default=0) #price in copper coins
    damage_type = models.CharField(blank=True, default="", max_length=100)
    properties = models.CharField(blank=True, default="", max_length=500)
    ammo = models.IntegerField(blank = True, default=0)

    def __str__(self) -> str:
        return self.weapon_name
#endregion

#region Armor
class Armor(GUIDModel):
    armor_name = models.CharField(default="", max_length=200)
    ca = models.IntegerField(default=11)
    is_damaged = models.BooleanField(default=False)
    price = models.IntegerField(default=0) #price in copper coins
    max_dex_modifier = models.IntegerField(default=2)
    required_force = models.IntegerField(default=0)
    disadvantage_stealth = models.BooleanField(default=False)
    disadvantage_athletism = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.armor_name
#endregion

#region Items
class Items(GUIDModel):
    item_name = models.CharField(default="", max_length=200)
    price = models.IntegerField(default=0) #price in copper coins
    is_homebrew = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.item_name
#endregion

#region Character
class Character(GUIDModel):
    ##Global
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    character_name = models.CharField(default="", max_length=200)
    description = models.TextField(blank=True, default="", max_length=5000)
    character_class_id = models.ForeignKey(CharacterClass, null=True, blank=True, on_delete=models.SET_NULL)
    character_species_id = models.ForeignKey(CharacterSpecies, null=True, blank=True, on_delete=models.SET_NULL)
    party_id = models.ForeignKey(Party, null=True, blank=True, on_delete=models.SET_NULL)

    ##Stats
    level = models.IntegerField(default=0)
    character_stats = models.ForeignKey(CharacterStats, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.character_name
#endregion

#region Character Weapon
class CharacterWeapon(GUIDModel):
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    weapon_type = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    nickname = models.CharField(blank=True, default="", max_length=100)
    is_equipped = models.BooleanField(default=False)
    ammo_count = models.IntegerField(blank = True, default=0)

    def __str__(self) -> str:
        return self.nickname if self.nickname else self.weapon_type.weapon_name
#endregion

#region Character Armor
class CharacterArmor(GUIDModel):
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    weapon_type = models.ForeignKey(Armor, on_delete=models.CASCADE)
    nickname = models.CharField(blank=True, default="", max_length=100)
    is_equipped = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nickname if self.nickname else self.weapon_type.armor_name
#endregion

#region Character Items
class CharacterItems(GUIDModel):
    character_id = models.ForeignKey(Character, null=True, blank=True, on_delete=models.SET_NULL)
    item_id = models.ForeignKey(Items, null=True, blank=True, on_delete=models.SET_NULL)
    nickname = models.CharField(blank=True, default="", max_length=100)
    is_item_hidden = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nickname if self.nickname else self.item_id.item_name
#endregion

#region Economy
class BankAccount(GUIDModel):
    bank_name = models.CharField(default="Player", max_length=100)
    account_name = models.CharField(null=True, blank=True, default="", max_length=100)
    owner = models.ManyToManyField(Character)
    
    ##Money
    copper_coins = models.IntegerField(null=True, blank=True, default=0)
    silver_coins = models.IntegerField(null=True, blank=True, default=0)
    gold_coins = models.IntegerField(null=True, blank=True, default=0)
    platinum_coins = models.IntegerField(null=True, blank=True, default=0)
    electrum_coins = models.IntegerField(null=True, blank=True, default=0)

    item = models.ManyToManyField(Items, blank=True)

    def __str__(self) -> str:
        bank_suffix = " [" + self.bank_name + "]" if self.bank_name else ""
        return (self.account_name + bank_suffix)
#endregion