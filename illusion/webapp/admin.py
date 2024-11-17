from django.contrib import admin
from .models import (
    BaseSystem, User, Campaign, Party, DM,
    CharacterClass, CharacterSpecies, Aptitude, Spell,
    Weapon, Armor, Items, Character, Skill, SkillSet,
    CharacterWeapon, CharacterArmor, CharacterItems, CharacterStats
)


admin.site.register(BaseSystem)
admin.site.register(User)
admin.site.register(Campaign)
admin.site.register(Party)
admin.site.register(DM)
admin.site.register(CharacterClass)
admin.site.register(CharacterSpecies)
admin.site.register(CharacterStats)
admin.site.register(Aptitude)
admin.site.register(Spell)
admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(Items)
admin.site.register(Character)
admin.site.register(Skill)
admin.site.register(SkillSet)
admin.site.register(CharacterWeapon)
admin.site.register(CharacterArmor)
admin.site.register(CharacterItems)