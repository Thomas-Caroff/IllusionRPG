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
        fields = ('__all__')

class CharacterClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterClass
        fields = ('pk', 'class_name', 'base_system_id', 'is_homebrew', 'hp_dice',
                'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'diplomacy')

class CharacterSpeciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterSpecies
        fields = ('pk', 'species_name', 'base_system_id', 'is_homebrew',
                'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'diplomacy')

class CharacterStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterStats
        fields = (
            'id',
            'strength',
            'str_mod',
            'dexterity', 
            'dex_mod',
            'constitution', 
            'con_mod',
            'intelligence', 
            'int_mod',
            'wisdom', 
            'wis_mod',
            'charisma', 
            'cha_mod',
            'diplomacy', 
            'dip_mod',
            'physic', 
            'social', 
            'mental', 
            'proficiency_bonus', 
            'skill_proficiency', 
            'skill_expertise')

class CharacterHealthSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterHealth
        fields = ("__all__")

class AptitudeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aptitude
        fields = ('pk', 'is_from_class', 'is_from_species', 'is_homebrew', 'aptitude_name', 'description')

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

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('pk', 'item_name', 'price', 'is_homebrew')

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ('pk', 'skill_name', 'is_saving_throw', "modified_by")

class SkillSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkillSet
        fields = ('pk', 'base_system_id', 'skill_list')

class BankAccountSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=Character.objects.all(), many=True)
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), many=True)

    class Meta:
        model = BankAccount
        fields = '__all__'
