from django.contrib import admin
from .models import User, Character, Campaign, Party, BaseSystem, DM

admin.site.register(User)
admin.site.register(Character)
admin.site.register(Campaign)
admin.site.register(Party)
admin.site.register(BaseSystem)
admin.site.register(DM)