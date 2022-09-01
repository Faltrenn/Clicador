from django.forms import ModelForm
from .models import Like, Match, Player

# Create the form class.
class PlayerForm(ModelForm):
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
        

