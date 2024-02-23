from rest_framework import serializers
from webapp.models import User, Character, Party, Campaign, BaseSystem, DM

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