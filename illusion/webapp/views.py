from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the main page index.")

def character_detail(request, character_id):
    return HttpResponse(f"You're searching for character {character_id}")

def user_profile(request, user_id):
    return HttpResponse(f"You're searching for user {user_id}")
