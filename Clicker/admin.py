from django.contrib import admin

from Clicker.models import Dislike, Like, Match, Player

# Register your models here.

admin.site.register(Player)
admin.site.register(Dislike)
admin.site.register(Like)
admin.site.register(Match)
