from django.shortcuts import render, redirect

from Clicker.form import LikeForm, MatchForm, PlayerForm
from Clicker.models import Dislike, Like, Match

# Create your views here.

def ordem(e):
  return e[0].score

def page1(pack):
    playerForm = PlayerForm()
    likeForm = LikeForm()
    pack["playerForm"] = playerForm
    pack["likeForm"] = likeForm
    listOfMatches = []

    for match in Match.objects.all():
        likes = dislikes = 0
        for like in Like.objects.all():
            if like.match_id == match:
                likes += 1
        for dislike in Dislike.objects.all():
            if dislike.match_id == match:
                dislikes += 1

        listOfMatches.append([match, likes, dislikes])
    listOfMatches.sort(key=ordem, reverse=True)
    pack["matches"] = listOfMatches
    return pack

def index(request):
    pack = {"player_id": None, "form": None, "matches": None, "likes": None}
    if request.method == "POST":
        if request.POST.get("name") is not None:
            form = PlayerForm(request.POST)
            if form.is_valid():
                form.save()
            pack["player_name"] = form["name"]
        else:
            match = Match.objects.get(pk=request.POST["match_id"])
            if request.POST["type"] == "like":
                like = Like(match_id = match)
                like.save()
            else:
                dislike = Dislike(match_id = match)
                dislike.save()

            pack = page1(pack)
    else:
        pack = page1(pack)
        
    return render(request, "index.html", pack)

def save(request):
    if request.method == "POST" :
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("index")
