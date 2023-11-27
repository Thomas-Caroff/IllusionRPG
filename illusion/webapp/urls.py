from django.urls import path

from . import views

urlpatterns = [
    path("", views.hompage, name="homepage"),
    path("character/<str:character_id>", views.character_detail, name="character"),
    path("user/<str:user_id>", views.user_profile, name="user"),
]