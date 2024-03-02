from rest_framework import serializers
from webapp.models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'pseudo', 'party_list')

class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = ('pk', 'campaign_name', 'quadgram', 'base_system_id', 'description')

class BaseSystemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseSystem
        fields = ('pk', 'system_name', 'url')

class PartySerializer(serializers.ModelSerializer):

    class Meta:
        model = Party
        fields = ('pk', 'party_name', 'campaign_id')

class DMSerializer(serializers.ModelSerializer):

    class Meta:
        model = DM
        fields = ('pk', 'user_id', 'party_id')

class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = ('pk', 'user_id', 'character_name', 'description',
                'character_class_id', 'character_race_id', 'party_id', 
                'copper_coins', 'silver_coins', 'gold_coins', 'platinum_coins',
                'level', 'proficiency_bonus',
                'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'diplomacy')

class CharacterClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterClass
        fields = ('pk', 'class_name', 'base_system_id', 'is_homebrew', 'hp_dice',
                'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'diplomacy')

class CharacterRaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterRace
        fields = ('pk', 'race_name', 'base_system_id', 'is_homebrew',
                'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'diplomacy')

class AptitudeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aptitude
        fields = ('pk', 'is_from_class', 'is_from_race', 'is_homebrew', 'aptitude_name', 'description')

class SpellSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spell
        fields = ('pk', 'spell_name', 'damages', 'level', 'property', 'is_bonus_action', 'is_homebrew')

class WeaponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weapon
        fields = ('pk', 'weapon_name', 'damages', 'damage_type', 'is_damaged', 'price', 'properties', 'ammo')

class ArmorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Armor
        fields = ('pk', 'armor_name', 'ca', 'max_dex_modifier', 'is_damaged', 'price', 'required_force', 'disadvantage_stealth', 'disadvantage_athletism')

class CharacterWeaponSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterWeapon
        fields = ('pk', 'character_id', 'weapon_type', 'nickname', 'is_equipped', 'ammo_count')

class CharacterArmorSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterArmor
        fields = ('pk', 'character_id', 'weapon_type', 'nickname', 'is_equipped')

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Items
        fields = ('pk', 'item_name', 'price', 'is_homebrew')