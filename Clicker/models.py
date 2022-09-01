from statistics import mode
from turtle import ondrag
from unicodedata import name
from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=12, primary_key=True)

class Match(models.Model):
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

class Like(models.Model):
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)

class Dislike(models.Model):
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
