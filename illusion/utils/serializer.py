from rest_framework import serializers
from webapp.models import User, Character, Party, Campaign

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'pseudo', 'party_list')