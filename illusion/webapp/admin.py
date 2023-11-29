from django.contrib import admin
from .models import User, Character, Campaign, Party

admin.site.register(User)
admin.site.register(Character)
admin.site.register(Campaign)
admin.site.register(Party)