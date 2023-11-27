from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Character

def hompage(request):
    userList = User.objects.order_by("username")
    characterList = Character.objects.order_by("-level")
    context = {"userList": userList, "characterList": characterList}
    return render(request, "illusion/homepage.html", context)

def character_detail(request, character_id):
    return HttpResponse(f"You're searching for character {character_id}")

def user_profile(request, user_id):
    return HttpResponse(f"You're searching for user {user_id}")
