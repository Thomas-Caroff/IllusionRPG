from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("character_view/<str:character_id>", views.character_detail, name="character"),
    path("user_profile/<str:user_id>", views.user_profile, name="user"),
    re_path(r"^user/$", views.userList),
    re_path(r"^user/([a-z0-9]*)$", views.user),
    re_path(r"^campaign/$", views.campaignList),
    re_path(r"^campaign/([a-z0-9]*)$", views.campaign),
    re_path(r"^basesystem/", views.baseSystemList),
    re_path(r"^basesystem/([a-z0-9]*)$", views.baseSystem),
    re_path(r"^party/$", views.partyList),
    re_path(r"^party/([a-z0-9]*)$", views.party),
    re_path(r"^character/$", views.characterList),
    re_path(r"^character/([a-z0-9]*)$", views.character),
    re_path(r"^aptitude/$", views.aptitudeList),
    re_path(r"^aptitude/([a-z0-9]*)$", views.aptitude),
    re_path(r"^spell/$", views.spellList),
    re_path(r"^spell/([a-z0-9]*)$", views.spell),
    re_path(r"^weapon/$", views.weaponList),
    re_path(r"^weapon/([a-z0-9]*)$", views.weapon),
    re_path(r"^armor/$", views.armorList),
    re_path(r"^armor/([a-z0-9]*)$", views.armor),
    re_path(r"^characterweapon/$", views.characterWeaponList),
    re_path(r"^characterweapon/([a-z0-9]*)$", views.characterWeapon),
    re_path(r"^characterarmor/$", views.characterArmorList),
    re_path(r"^characterarmor/([a-z0-9]*)$", views.characterArmor),
]