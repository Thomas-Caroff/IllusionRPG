from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Character
import utils.datastorer as ds

def hompage(request):
    userList = User.objects.order_by("username")
    characterList = Character.objects.order_by("-level")
    context = {"userList": userList, "characterList": characterList}
    return render(request, "illusion/homepage.html", context)

def character_detail(request, character_id):
    return HttpResponse(f"You're searching for character {character_id}")

def user_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    party_list = ds.quadgram_extracter(user.party_list)
    Character_list = Character.objects.filter(user_id=user_id)
    context = {"user": user, "party_list": party_list, "character_list": Character_list}
    return render(request, "illusion/userpage.html", context)
