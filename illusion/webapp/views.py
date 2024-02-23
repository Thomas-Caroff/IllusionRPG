from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User, Character, Party, Campaign
import utils.datastorer as ds
from utils.serializer import *
import utils.customUUID as cuuid

@api_view(['GET'])
def user_list(request):
    data = User.objects.order_by("username")
    serialUserList = UserSerializer(data, context={'request': request}, many=True)
    return Response(serialUserList.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user(request, pk):
    if request.method == 'GET':
        data = User.objects.filter(pk=pk)
        serializer = UserSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        request.data['pk'] = cuuid.custom_id()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def campaign(request, pk):
    if request.method == 'GET':
        data = Campaign.objects.filter(pk=pk)
        serializer = CampaignSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        request.data['pk'] = cuuid.custom_id()
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        campaign = Campaign.objects.get(pk=pk)
    except Campaign.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CampaignSerializer(campaign, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        campaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def baseSystem(request, pk):
    if request.method == 'GET':
        data = BaseSystem.objects.filter(pk=pk)
        serializer = BaseSystemSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def baseSystemList(request):
    if request.method == 'GET':
        data = BaseSystem.objects.all()
        serializer = BaseSystemSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def campaign(request, pk):
    if request.method == 'GET':
        data = Campaign.objects.filter(pk=pk)
        serializer = CampaignSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        request.data['pk'] = cuuid.custom_id()
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        campaign = Campaign.objects.get(pk=pk)
    except Campaign.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CampaignSerializer(campaign, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        campaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def party(request, pk):
    if request.method == 'GET':
        data = Party.objects.filter(pk=pk)
        serializer = PartySerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        request.data['pk'] = cuuid.custom_id()
        serializer = PartySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        party = Party.objects.get(pk=pk)
    except Party.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PartySerializer(party, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        party.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def dm(request, pk):
    if request.method == 'GET':
        data = DM.objects.filter(pk=pk)
        serializer = DMSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        request.data['pk'] = cuuid.custom_id()
        serializer = DMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        dm = DM.objects.get(pk=pk)
    except DM.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DM(dm, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        dm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
