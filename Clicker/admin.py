from django.contrib import admin

from Clicker.models import Hint, Like, Match, Player

# Register your models here.

admin.site.register(Player)
admin.site.register(Hint)
admin.site.register(Like)
admin.site.register(Match)
