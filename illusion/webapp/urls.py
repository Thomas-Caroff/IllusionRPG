from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("character/<str:character_id>", views.character_detail, name="character"),
    path("user_profile/<str:user_id>", views.user_profile, name="user"),
    re_path(r"^user/$", views.user_list),
    re_path(r"^user/([a-z0-9]*)$", views.user),
    re_path(r"^campaign/([a-z0-9]*)$", views.campaign),
    re_path(r"^basesystem/", views.baseSystemList),
    re_path(r"^basesystem/([a-z0-9]*)$", views.baseSystem),
    re_path(r"^party/([a-z0-9]*)$", views.party),
]