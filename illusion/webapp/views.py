from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Character, Party, Campaign
import utils.datastorer as ds

def homepage(request):
    userList = User.objects.order_by("username")
    characterList = Character.objects.order_by("-level")
    context = {"userList": userList, "characterList": characterList}
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
