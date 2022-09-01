from django.forms import ModelForm, CharField, TextInput
from .models import Like, Match, Player

# Create the form class.
class PlayerForm(ModelForm):
    name = CharField(label='', widget=TextInput(attrs={"placeholder": "Digite seu nome"}))
    class Meta:
        model = Player
        fields = ["name"]

class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = ["player_id", "score"]

class LikeForm(ModelForm):
    class Meta:
        model = Like
        fields = ["match_id"]
        

