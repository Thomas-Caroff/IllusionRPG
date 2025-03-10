#region IMPORTS
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
import utils.datastorer as ds
from utils.serializer import *
import utils.customUUID as cuuid
#endregion

def requestHandler(request, Model, Serializer, pk=None):
    if request.method == 'GET':
        data = Model.objects.filter(pk=pk)
        serializer = Serializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        request.data['pk'] = cuuid.custom_id()
        serializer = Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        model = Model.objects.get(pk=pk)
    except Model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = Serializer(model, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#region USER
@api_view(['GET'])
def userList(request):
    data = User.objects.values("pk", "username")
    serialUserList = UserSerializer(data, context={'request': request}, many=True)
    return Response(serialUserList.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user(request, pk):
    return requestHandler(request, User, UserSerializer, pk)
#endregion

#region CAMPAIGN
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def campaign(request, pk):
    return requestHandler(request, Campaign, CampaignSerializer, pk)

@api_view(['GET'])
def campaignList(request):
    if request.method == 'GET':
        data = Campaign.objects.values("pk", "quadgram")
        serializer = CampaignSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
#endregion

#region BASE SYSTEM
@api_view(['GET'])
def baseSystem(request, pk):
    return requestHandler(request, BaseSystem, BaseSystemSerializer, pk)

@api_view(['GET'])
def baseSystemList(request):
    if request.method == 'GET':
        data = BaseSystem.objects.values("pk", "system_name")
        serializer = BaseSystemSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
#endregion

#region PARTY
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def party(request, pk):
    return requestHandler(request, Party, PartySerializer, pk)

@api_view(['GET'])
def partyList(request):
    if request.method == 'GET':
        data = Party.objects.values("pk", "party_list")
        serializer = PartySerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
#endregion

#region DM
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def dm(request, pk):
    return requestHandler(request, DM, DMSerializer, pk)

@api_view(['GET'])
def dmList(request):
    if request.method == 'GET':
        data = DM.objects.all()
        serializer = DMSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
#endregion

#region CHARACTER
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def character(request, pk):
    return requestHandler(request, Character, CharacterSerializer, pk)

@api_view(['GET'])
def characterList(request):
    if request.method == 'GET':
        data = Character.objects.only("pk", "user_id", "character_name", "character_class_id", "character_species_id")
        serializer = CharacterSerializer(data, context={'request': request}, many=True)

        # Filtering to only send minimal data
        filtered_data = [
            {key: item[key] for key in ["pk", "user_id", "character_name", "character_class_id", "character_species_id"]}
            for item in serializer.data
        ]
        
        return Response(filtered_data)

#region CLASS
@api_view(['GET'])
def characterClassList(request):
    if request.method == 'GET':
        data = CharacterClass.objects.values("pk", "class_name")
        serializer = CharacterClassSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def characterClass(request, pk):
    return requestHandler(request, CharacterClass, CharacterClassSerializer, pk)
#endregion CLASS

#region SPECIES
@api_view(['GET'])
def characterSpeciesList(request):
    if request.method == 'GET':
        data = CharacterSpecies.objects.values("pk", "species_name")
        serializer = CharacterSpeciesSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def characterSpecies(request, pk):
    return requestHandler(request, CharacterSpecies, CharacterSpeciesSerializer, pk)
#endregion SPRECIES

#region STATS
@api_view(['GET'])
def characterStatsList(request):
    if request.method == 'GET':
        data = CharacterStats.objects.values("pk")
        serializer = CharacterStatsSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def characterStats(request, pk):
    return requestHandler(request, CharacterStats, CharacterStatsSerializer, pk)
#endregion STATS

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def characterHealth(request, pk):
    return requestHandler(request, CharacterHealth, CharacterHealthSerializer, pk)

@api_view(['GET'])
def characterHealthList(request):
    if request.method == 'GET':
        data = CharacterHealth.objects.values("pk")
        serializer = CharacterHealthSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

#region ITEM
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def item(request, pk):
    return requestHandler(request, Item, ItemSerializer, pk)

@api_view(['GET'])
def itemList(request):
    if request.method == 'GET':
        data = Item.objects.values("pk", "item_name")
        serializer = ItemSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
#endregion ITEM

#region SKILLS
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def skill(request, pk):
    return requestHandler(request, Skill, SkillSerializer, pk)

@api_view(['GET'])
def skillList(request):
    if request.method == 'GET':
        data = Skill.objects.all()
        serializer = SkillSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def skillSet(request, pk):
    return requestHandler(request, SkillSet, SkillSetSerializer, pk)

@api_view(['GET'])
def skillSetList(request):
    if request.method == 'GET':
        data = SkillSet.objects.values("pk", "base_system_id")
        serializer = SkillSetSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
#endregion

#region APTITUDE
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def aptitude(request, pk):
    return requestHandler(request, Aptitude, AptitudeSerializer, pk)

@api_view(['GET'])
def aptitudeList(request):
    if request.method == 'GET':
        data = Aptitude.objects.values("pk", "aptitude_name")
        serializer = AptitudeSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
#endregion

#region SPELL
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def spell(request, pk):
    return requestHandler(request, Spell, SpellSerializer, pk)

@api_view(['GET'])
def spellList(request):
    if request.method == 'GET':
        data = Spell.objects.values("pk", "spell_name")
        serializer = SpellSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
#endregion

#region WEAPON
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def weapon(request, pk):
    return requestHandler(request, Weapon, WeaponSerializer, pk)

@api_view(['GET'])
def weaponList(request):
    if request.method == 'GET':
        data = Weapon.objects.values("pk", "weapon_name")
        serializer = WeaponSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
#endregion

#region ARMOR
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def armor(request, pk):
    return requestHandler(request, Armor, ArmorSerializer, pk)

@api_view(['GET'])
def armorList(request):
    if request.method == 'GET':
        data = Armor.objects.values("pk", "armor_name")
        serializer = ArmorSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
#endregion

#endregion CHARACTER

#region BANK ACCOUNT
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def bankAccount(request, pk):
    return requestHandler(request, BankAccount, BankAccountSerializer, pk)

@api_view(['GET'])
def bankAccountList(request, character_pk):
    if request.method == 'GET':
        try:
            character = Character.objects.get(pk=character_pk)
        except Character.DoesNotExist:
            return Response(
                {"error": "Character not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        data = BankAccount.objects.filter(owner=character)
        serializer = BankAccountSerializer(data, many=True, context={'request': request})
        return Response(serializer.data)
#endregion



########################################################################################

def homepage(request):
    userList = User.objects.order_by("username")
    characterList = Character.objects.order_by("-level")
    context = {"userList": userList, "characterList": characterList, "title": "Bienvenue sur IllusionJDR"}
    return render(request, "illusion/homepage.html", context)

def party_detail(request, party_id):
    return HttpResponse(f"You're searching for party {party_id}")

def campaign_overview(request, campaign_id):
    return HttpResponse(f"You're searching for campaign {campaign_id}")

def character_detail(request, character_id):
    character = Character.objects.get(pk=character_id)
    user = User.objects.get(pk=character.user_id)
    party = Party.objects.get(pk=character.party_id)
    campaign = Campaign.objects.get(pk=party.campaign_id)
    context = {"character": character, "user": user, "party": party, "campaign": campaign}
    return render(request, "illusion/character.html", context)

def user_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    party_list = ds.quadgram_extracter(user.party_list)
    Character_list = Character.objects.filter(user_id=user_id)
    context = {"user": user, "party_list": party_list, "character_list": Character_list}
    return render(request, "illusion/userpage.html", context)
